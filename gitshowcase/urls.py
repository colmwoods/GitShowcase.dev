"""
URL configuration for gitshowcase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home, name='home'),
    path('about/', views.about, name='about'),
    path("api/star/", views.star_repo, name="star_repo"),
    path("search/", views.search, name="search"),
    path("add_bookmark/", views.add_bookmark, name="add_bookmark"),
    path('bookmarks/', views.bookmark_list, name='bookmarks'),
    path('delete_bookmark/<int:bookmark_id>/', views.delete_bookmark, name='delete_bookmark'),
    path("comment/add/", views.add_comment, name="add_comment"),
    path("comment/edit/<int:comment_id>/", views.edit_comment, name="edit_comment"),
    path("comment/delete/<int:comment_id>/", views.delete_comment, name="delete_comment"),
]
