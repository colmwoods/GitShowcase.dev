from django.contrib import admin
from .models import Bookmark, Comment

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("user", "repo_name", "repo_url", "language", "created_at")
    search_fields = ("repo_name", "repo_url", "language")
    list_filter = ("language", "created_at")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "repo_name", "body", "created_at")
    search_fields = ("repo_name", "body", "user__username")
    list_filter = ("created_at",)