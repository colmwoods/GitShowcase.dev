from django.apps import AppConfig


class GitshowcaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "gitshowcase"

    def ready(self):
        import gitshowcase.signals