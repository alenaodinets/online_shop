from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product


class ProdListView(ListView):
    model = Product


class ProdDetailView(DetailView):
    model = Product


class ProdCreateView(CreateView):
    model = Product
    fields = ("name", "description", "price", "category", "image_preview")
    success_url = reverse_lazy("catalog:prod_list")


class ProdUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "price", "category", "image_preview")
    success_url = reverse_lazy("catalog:prod_list")


class ProdDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:prod_list")


def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    return render(request, "catalog/contacts.html")
