from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product


class ProdListView(ListView):
    model = Product


class ProdDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProdCreateView(CreateView):
    model = Product
    fields = ("name", "description", "price", "category", "image_preview")
    success_url = reverse_lazy("catalog:prod_list")


class ProdUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "price", "category", "image_preview")
    success_url = reverse_lazy("catalog:prod_list")

    def get_success_url(self):
        return reverse("catalog:prod_detail", args=[self.kwargs.get("pk")])


class ProdDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:prod_list")


def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    return render(request, "catalog/contacts.html")
