from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount, SocialToken
import requests
import json
from datetime import datetime
from .models import Bookmark, Comment
from .forms import CommentForm

# ---------------- HOME PAGE ----------------
def home(request):
    repos = []
    comments_by_repo = {}
    bookmarked_urls = []

    if request.user.is_authenticated:
        try:
            social_account = SocialAccount.objects.get(user=request.user, provider='github')
            token = SocialToken.objects.get(account=social_account, account__user=request.user)

            url = (
                "https://api.github.com/user/repos"
                "?visibility=all"
                "&affiliation=owner,collaborator,organization_member"
                "&sort=updated"
                "&direction=desc"
                "&per_page=100"
            )

            headers = {
                "Authorization": f"token {token.token}",
                "Accept": "application/vnd.github+json",
            }

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                for repo in data:
                    updated = repo.get("updated_at")
                    if updated:
                        try:
                            repo["updated_at"] = datetime.strptime(updated, "%Y-%m-%dT%H:%M:%SZ")
                        except ValueError:
                            repo["updated_at"] = None
                    repos.append(repo)
            else:
                print("❌ GitHub API error:", response.status_code, response.text[:300])

            # ✅ Collect comments for displayed repos
            repo_names = [r.get("name") for r in repos if "name" in r]
            if repo_names:
                comments = Comment.objects.filter(repo_name__in=repo_names)
                for comment in comments:
                    comments_by_repo.setdefault(comment.repo_name, []).append(comment)

            bookmarked_urls = list(
                Bookmark.objects.filter(user=request.user).values_list("repo_url", flat=True)
            )

        except Exception as e:
            print("💥 GitHub API exception:", e)

    return render(
        request,
        "home.html",
        {
            "repos": repos,
            "comments_by_repo": comments_by_repo,
            "bookmarked_urls": bookmarked_urls,
        },
    )



# ---------------- ABOUT PAGE ----------------
def about(request):
    return render(request, "about.html")


# ---------------- STAR REPO ENDPOINT ----------------
@login_required
@require_POST
def star_repo(request):
    """Star a GitHub repository using the authenticated user's token."""
    try:
        data = json.loads(request.body.decode())
        repo_full_name = data.get("repo")

        if not repo_full_name:
            return JsonResponse({"ok": False, "error": "Missing repo name"}, status=400)

        social_account = SocialAccount.objects.get(user=request.user, provider='github')
        token = SocialToken.objects.get(account=social_account, account__user=request.user)

        url = f"https://api.github.com/user/starred/{repo_full_name}"
        headers = {
            "Authorization": f"token {token.token}",
            "Accept": "application/vnd.github+json",
        }

        response = requests.put(url, headers=headers)

        if response.status_code in (204, 304):
            return JsonResponse({"ok": True})
        else:
            return JsonResponse(
                {"ok": False, "status": response.status_code, "body": response.text[:200]},
                status=400,
            )

    except Exception as e:
        return JsonResponse({"ok": False, "error": str(e)}, status=500)
    
# ---------------- SEARCH PAGE ----------------
def search(request):
    repos = []
    user_data = None
    comments_by_repo = {}
    bookmarked_urls = []
    query = request.GET.get("q", "").strip()

    if query:
        user_url = f"https://api.github.com/users/{query}"
        repos_url = f"https://api.github.com/users/{query}/repos?per_page=100&sort=updated&direction=desc"
        headers = {"Accept": "application/vnd.github+json"}

        user_response = requests.get(user_url, headers=headers)
        repos_response = requests.get(repos_url, headers=headers)

        # ✅ Fetch GitHub user info
        if user_response.status_code == 200:
            user_data = user_response.json()

        # ✅ Fetch repositories
        if repos_response.status_code == 200:
            repos = repos_response.json()

            for repo in repos:
                updated = repo.get("updated_at")
                if updated:
                    try:
                        repo["updated_at"] = datetime.strptime(updated, "%Y-%m-%dT%H:%M:%SZ")
                    except ValueError:
                        repo["updated_at"] = None

            # ✅ Collect comments for repos found
            repo_names = [r.get("name") for r in repos if "name" in r]
            if repo_names:
                comments = Comment.objects.filter(repo_name__in=repo_names)
                for comment in comments:
                    comments_by_repo.setdefault(comment.repo_name, []).append(comment)

        if request.user.is_authenticated:
            bookmarked_urls = list(
                Bookmark.objects.filter(user=request.user).values_list("repo_url", flat=True)
        )

    return render(
        request,
        "search.html",
        {
            "repos": repos,
            "query": query,
            "user_data": user_data,
            "comments_by_repo": comments_by_repo,
            "bookmarked_urls": bookmarked_urls,
        },
    )


# ---------------- BOOKMARKS ----------------
@login_required(login_url='/accounts/login/')
def add_bookmark(request):
    if request.method == 'POST':
        repo_name = request.POST.get('repo_name')
        repo_url = request.POST.get('repo_url')

        # Avoid duplicates
        if Bookmark.objects.filter(user=request.user, repo_url=repo_url).exists():
            messages.info(request, f"'{repo_name}' is already bookmarked.")
            return redirect('bookmarks')

        # Try to fetch GitHub data
        github_data = {}
        try:
            # repo_name may be like 'owner/repo'
            if '/' not in repo_name and 'github.com/' in repo_url:
                repo_name = repo_url.split('github.com/')[-1]
            api_url = f"https://api.github.com/repos/{repo_name}"
            response = requests.get(api_url, timeout=5)
            if response.status_code == 200:
                github_data = response.json()
        except Exception as e:
            print(f"GitHub API fetch failed: {e}")

        Bookmark.objects.create(
            user=request.user,
            repo_name=repo_name,
            repo_url=repo_url,
            language=github_data.get('language'),
            description=github_data.get('description'),
            stargazers_count=github_data.get('stargazers_count', 0),
            forks_count=github_data.get('forks_count', 0),
        )

        messages.success(request, f"'{repo_name}' has been bookmarked.")
        return redirect('bookmarks')

    return redirect('home')

@login_required(login_url='/accounts/login/')
def bookmark_list(request):
    bookmarks = Bookmark.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookmarks.html', {'bookmarks': bookmarks})

@login_required(login_url='/accounts/login/')
def delete_bookmark(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, id=bookmark_id, user=request.user)
    bookmark.delete()
    return redirect('bookmarks')

# ---------------- COMMENTS ----------------
@login_required
def add_comment(request):
    """
    Create a new comment for a repository.
    """
    if request.method == "POST":
        repo_name = request.POST.get("repo_name")
        repo_url = request.POST.get("repo_url")
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.repo_name = repo_name
            comment.repo_url = repo_url
            comment.save()
            messages.success(request, "💬 Comment added successfully!")
        else:
            messages.error(request, "❌ Failed to add comment.")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def edit_comment(request, comment_id):
    """
    Edit an existing comment.
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user != request.user:
        messages.error(request, "You can only edit your own comments.")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()  # ✅ simplified — no extra logic
            messages.success(request, "✏️ Comment updated successfully!")
        else:
            messages.error(request, "❌ Failed to update comment.")
    else:
        messages.error(request, "❌ Invalid request.")

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def delete_comment(request, comment_id):
    """
    Delete a comment.
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user != request.user:
        messages.error(request, "You can only delete your own comments.")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

    comment.delete()
    messages.success(request, "🗑️ Comment deleted successfully.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))