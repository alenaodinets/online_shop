from django.urls import path

from catalog.views import home, contacts
from catalog.views import prod_list, prod_detail
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", prod_list, name='prod_list'),
    path("catalog/<int:pk>/", prod_detail, name='prod_detail'),
    path("home/", home),
    path("contacts/", contacts),
]
