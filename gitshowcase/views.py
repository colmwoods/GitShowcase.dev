# /views.py
# Handles homepage (fetches GitHub repos) and About page

from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount, SocialToken
import requests
from datetime import datetime


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

        except Exception as e:
            print("GitHub API exception:", e)

    return render(request, "home.html", {"repos": repos})


def about(request):
    return render(request, "about.html")