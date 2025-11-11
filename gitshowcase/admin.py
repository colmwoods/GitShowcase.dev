from django.contrib import admin
from .models import Bookmark, Comment, ContactMessage
import requests


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    fields = ("user", "repo_url")
    list_display = ("user", "repo_name", "language", "stargazers_count", "forks_count")

    def save_model(self, request, obj, form, change):
        """Auto-fill all bookmark info from GitHub when only repo_url is given."""
        if obj.repo_url:
            try:
                repo_full_name = obj.repo_url.replace("https://github.com/", "").strip("/")
                response = requests.get(f"https://api.github.com/repos/{repo_full_name}")
                if response.status_code == 200:
                    data = response.json()
                    obj.repo_name = data.get("name", "")
                    obj.language = data.get("language", "")
                    obj.description = data.get("description", "")
                    obj.stargazers_count = data.get("stargazers_count", 0)
                    obj.forks_count = data.get("forks_count", 0)
                else:
                    print(f"⚠️ GitHub API returned {response.status_code} for {repo_full_name}")
            except Exception as e:
                print("⚠️ Error fetching GitHub repo data:", e)

        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "repo_link", "body", "created_at")
    search_fields = ("repo_url", "user__username", "body")
    fields = ("user", "repo_url", "body")  # Only show these in Add/Edit form

    def repo_link(self, obj):
        return f'<a href="{obj.repo_url}" target="_blank">{obj.repo_url}</a>'
    repo_link.allow_tags = True
    repo_link.short_description = "Repository URL"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'message')
