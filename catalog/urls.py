from django.urls import path

from catalog.views import home, contacts
from catalog.views import ProdListView, ProdDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProdListView.as_view(), name="prod_list"),
    path("catalog/<int:pk>/", ProdDetailView.as_view(), name="prod_detail"),
    path("home/", home),
    path("contacts/", contacts),
]
