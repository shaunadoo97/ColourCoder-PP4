from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


# Create your views here.
class ArtPostList(generic.ListView):
     queryset = Post.objects.all()
     template_name = "artblog/artindex.html"
     paginate_by = 3

def artpost_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/artpost_detail.html",
        {"post": post},
    )