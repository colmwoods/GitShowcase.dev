from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount, SocialToken
import requests
import json
from datetime import datetime


# ---------------- HOME PAGE ----------------
def home(request):
    repos = []

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

        except Exception as e:
            print("💥 GitHub API exception:", e)

    return render(request, "home.html", {"repos": repos})


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

def search(request):
    query = request.GET.get("q", "").strip()
    results = []

    if query:
        results = [f"Result 1 for '{query}'", f"Result 2 for '{query}'", f"Result 3 for '{query}'"]

    return render(request, "search.html", {"query": query, "results": results})