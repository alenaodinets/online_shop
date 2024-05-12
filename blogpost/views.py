from django.urls import reverse_lazy
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


class BlogPostCreateView(CreateView):
    model = Blogpost
    fields = ("title", "slug", "content", "preview")
    success_url = reverse_lazy("blogpost:blogpost_form")

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.personal_manager = self.request.user
            new_blog.save()

        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = Blogpost
    fields = ("title", "slug", "content", "preview")
    success_url = reverse_lazy("blogpost:blogpost_form")


class BlogPostDeleteView(DeleteView):
    model = Blogpost
    success_url = reverse_lazy("blogpost:blogpost_list")
