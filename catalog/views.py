from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version
from catalog.sevices import get_products_from_cache


class ProdListView(ListView, LoginRequiredMixin):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = self.get_queryset(*args, **kwargs)
        for product in products:
            versions = Version.objects.filter(product=product)
            is_active_version = versions.filter(is_active_version=True)
            if is_active_version:
                product.active_version = is_active_version.last().name_of_versions
            else:
                product.active_version = 'Нет активной версии'

        context_data['object_list'] = products
        return context_data

    def get_queryset(self):
        return get_products_from_cache()


class ProdDetailView(DetailView, LoginRequiredMixin):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProdCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:prod_list")

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProdUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:prod_list")

    def get_success_url(self):
        return reverse("catalog:prod_detail", args=[self.kwargs.get("pk")])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = ProductFormset(instance=self.object)
        context['title'] = 'Изменить продукт'
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()

        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if (user.has_perm('catalog.set_published')
                and user.has_perm('catalog.change_description')
                and user.has_perm('catalog.change_category')):
            return ProductModeratorForm
        else:
            return PermissionDenied


class ProdDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy("catalog:prod_list")


def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    return render(request, "catalog/contacts.html")
