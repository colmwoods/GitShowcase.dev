from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added


@receiver(social_account_added)
def set_first_name_from_github(request, sociallogin, **kwargs):
    """Set the user's first name from their GitHub profile upon social account addition."""
    user = sociallogin.user
    account = sociallogin.account

    # Only run for GitHub
    if account.provider != "github":
        return

    data = account.extra_data or {}
    github_name = data.get("name")

    if github_name and not user.first_name:
        user.first_name = github_name.split()[0]
        user.save()
