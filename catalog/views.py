from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    return render(request, "catalog/contacts.html")


def prod_list(request):
    product = Product.objects.all()
    context = {"product": product}
    return render(request, "catalog/prod_list.html", context)


def prod_detail(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    context = {"prod": prod}
    return render(request, "catalog/prod_detail.html", context)
