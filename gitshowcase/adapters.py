from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib import messages
from django.shortcuts import redirect


class GitHubUsernameAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        """
        Runs BEFORE the user is saved.
        Prevents colm1 / colm4 usernames.
        """
        user = super().populate_user(request, sociallogin, data)

        if sociallogin.account.provider == "github":
            github_username = data.get("login")
            if github_username:
                user.username = github_username

            github_name = data.get("name")
            if github_name:
                user.first_name = github_name.split()[0]

        return user


def authentication_error(
    self,
    request,
    provider_id,
    error=None,
    exception=None,
    extra_context=None,
):
    """
    Handles OAuth cancellation or failure.
    Redirects user safely with feedback instead of Django default error page.
    """
    messages.warning(
        request,
        "GitHub login was cancelled or failed. No changes were made."
    )
    return redirect("home")
