from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount, SocialToken
import requests

def home(request):
    repos = []

    if request.user.is_authenticated:
        try:
            # Get the user's linked GitHub account + token
            social_account = SocialAccount.objects.get(user=request.user, provider='github')
            token = SocialToken.objects.get(account=social_account, account__user=request.user)

            print("🔍 Fetching repos for:", request.user.username)
            print("✅ Token in use:", token.token[:6] + "...")

            # Fetch all repositories (owned, collaborator, organization)
            url = (
                "https://api.github.com/user/repos"
                "?visibility=all"
                "&affiliation=owner,collaborator,organization_member"
                "&per_page=100"
            )

            headers = {
                'Authorization': f'token {token.token}',
                'Accept': 'application/vnd.github+json',
            }
            response = requests.get(url, headers=headers)
            print("📡 GitHub API status:", response.status_code)

            if response.status_code == 200:
                repos = response.json()
                print(f"📁 Repos fetched: {len(repos)}")

                if not repos:
                    print("⚠️ GitHub returned an empty list — possible visibility or scope issue.")
                    print("🔍 Partial response:", response.text[:500])
            else:
                print("❌ GitHub API error:", response.text[:500])

        except Exception as e:
            print("💥 GitHub API exception:", e)

    return render(request, 'home.html', {'repos': repos})


def about(request):
    return render(request, 'about.html')