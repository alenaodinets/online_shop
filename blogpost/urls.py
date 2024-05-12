from django.urls import path

from blogpost.views import BlogPostDeleteView, BlogPostUpdateView, \
    BlogPostListView, BlogPostCreateView, BlogPostDetailView
from blogpost.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", BlogPostListView.as_view(), name="blogpost_list"),
    path("blogpost/<int:pk>/", BlogPostDetailView.as_view(), name="blogpost_detail"),
    path("blogpost/create/", BlogPostCreateView.as_view(), name="blogpost_create"),
    path("blogpost/<int:pk>/update/", BlogPostUpdateView.as_view(), name="blogpost_update"),
    path("blogpost/<int:pk>/delete/", BlogPostDeleteView.as_view(), name="blogpost_delete"),
]