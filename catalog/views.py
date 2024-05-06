from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from catalog.models import Product


class ProdListView(ListView):
    model = Product


class ProdDetailView(DetailView):
    model = Product


def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    return render(request, "catalog/contacts.html")

