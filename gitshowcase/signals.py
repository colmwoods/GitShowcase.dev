from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added


@receiver(social_account_added)
def set_username_from_github(request, sociallogin, **kwargs):
    """
    Set the user's username to their GitHub username
    when a social account is added.
    """
    user = sociallogin.user
    account = sociallogin.account

    if account.provider != "github":
        return

    github_username = account.extra_data.get("login")

    if github_username and user.username != github_username:
        user.username = github_username
        user.save()