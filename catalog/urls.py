from django.urls import path

from catalog.views import home, contacts, ProdCreateView, ProdDeleteView
from catalog.views import ProdListView, ProdDetailView, ProdUpdateView
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
]
