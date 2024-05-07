from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Blogpost


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


class BlogPostListView(ListView):
    model = Blogpost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(publication_sign=True)
        return queryset


class BlogPostDetailView(DetailView):
    model = Blogpost


class BlogPostCreateView(CreateView):
    model = Blogpost
    fields = ("title", "slug", "content", "preview")
    success_url = reverse_lazy("catalog:blogpost_list")

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

class BlogPostUpdateView(UpdateView):
    model = Blogpost
    fields = ("title", "slug", "content", "preview")
    success_url = reverse_lazy("catalog:blogpost_list")


class BlogPostDeleteView(DeleteView):
    model = Blogpost
    success_url = reverse_lazy("catalog:blogpost_list")


def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    return render(request, "catalog/contacts.html")
