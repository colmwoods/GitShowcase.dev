from django.shortcuts import redirect
from allauth.socialaccount.providers.github.views import oauth2_login

def github_redirect(request):
    return oauth2_login(request)
