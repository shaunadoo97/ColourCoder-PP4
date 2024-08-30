from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post



# Create your views here.
class ArtPostList(generic.ListView):
     queryset = Post.objects.all()
     template_name = "artblog/artindex.html"
     paginate_by = 3

def artpost_detail(request, slug):
  
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments= post.comments.all().order_by("created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    return render(
        request,
        "blog/artpost_detail.html",
        {"post": post,
         "comments": comments,
         "comment_count": comment_count, 
         "comment_form": comment_form,},
        
    )