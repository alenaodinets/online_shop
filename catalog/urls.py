from django.urls import path

from catalog.views import home, contacts, ProdCreateView, ProdDeleteView
from catalog.views import ProdListView, ProdDetailView, ProdUpdateView, BlogPostDeleteView, BlogPostUpdateView, \
    BlogPostListView, BlogPostCreateView, BlogPostDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProdListView.as_view(), name="prod_list"),
    path("catalog/<int:pk>/", ProdDetailView.as_view(), name="prod_detail"),
    path("home/", home),
    path("contacts/", contacts),
    path("catalog/create/", ProdCreateView.as_view(), name="prod_create"),
    path("catalog/<int:pk>/update/", ProdUpdateView.as_view(), name="prod_update"),
    path("catalog/<int:pk>/delete/", ProdDeleteView.as_view(), name="prod_delete"),
    path("", BlogPostListView.as_view(), name="blogpost_list"),
    path("catalog/<int:pk>/", BlogPostDetailView.as_view(), name="blogpost_detail"),
    path("catalog/create/", BlogPostCreateView.as_view(), name="blogpost_create"),
    path("catalog/<int:pk>/update/", BlogPostUpdateView.as_view(), name="blogpost_update"),
    path("catalog/<int:pk>/delete/", BlogPostDeleteView.as_view(), name="blogpost_delete"),
]
