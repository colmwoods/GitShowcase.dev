from django.contrib import admin
from .models import Bookmark, Comment


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("user", "repo_link", "created_at")
    search_fields = ("repo_url", "user__username")
    fields = ("user", "repo_url")  # Only show these in Add/Edit form

    def repo_link(self, obj):
        return f'<a href="{obj.repo_url}" target="_blank">{obj.repo_url}</a>'
    repo_link.allow_tags = True
    repo_link.short_description = "Repository URL"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "repo_link", "body", "created_at")
    search_fields = ("repo_url", "user__username", "body")
    fields = ("user", "repo_url", "body")  # Only show these in Add/Edit form

    def repo_link(self, obj):
        return f'<a href="{obj.repo_url}" target="_blank">{obj.repo_url}</a>'
    repo_link.allow_tags = True
    repo_link.short_description = "Repository URL"
