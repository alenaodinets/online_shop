from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blogpost.models import Blogpost


class BlogPostListView(ListView):
    model = Blogpost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(publication_sign=True)
        return queryset


class BlogPostDetailView(DetailView):
    model = Blogpost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = Blogpost
    fields = ("title", "slug", "content", "preview")
    success_url = reverse_lazy("blogpost:blogpost_list")

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = Blogpost
    fields = ("title", "slug", "content", "preview")
    success_url = reverse_lazy("blogpost:blogpost_list")

    def get_success_url(self):
        return reverse_lazy("blogpost:blogpost_list")


class BlogPostDeleteView(DeleteView):
    model = Blogpost
    success_url = reverse_lazy("blogpost:blogpost_list")
