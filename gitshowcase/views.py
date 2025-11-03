from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount, SocialToken
import requests

def home(request):
    repos = []

    if request.user.is_authenticated:
        try:
            social_account = SocialAccount.objects.get(user=request.user, provider='github')
            token = SocialToken.objects.get(account=social_account, account__user=request.user)
            headers = {
                'Authorization': f'token {token.token}',
                'Accept': 'application/vnd.github+json',
            }
            response = requests.get('https://api.github.com/user/repos', headers=headers)

            if response.status_code == 200:
                repos = response.json()
        except Exception as e:
            print("GitHub API error:", e)

    return render(request, 'home.html', {'repos': repos})

def about(request):
    return render(request, 'about.html')