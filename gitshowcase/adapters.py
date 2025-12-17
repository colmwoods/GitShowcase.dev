from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class GitHubUsernameAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        """
        This runs BEFORE the user is saved.
        We set username here so colm4 is NEVER created.
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
