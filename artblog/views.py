from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm
from .forms import PostForm



# Create your views here.
class ArtPostList(generic.ListView):
     queryset = Post.objects.all()
     template_name = "artblog/artindex.html"
     paginate_by = 3

def artpost_detail(request, slug):
  
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

    comment_form = CommentForm()

    return render(
        request,
        "artblog/artpost_detail.html",
        {
          "post": post,
          "comments": comments, 
          "comment_count": comment_count,
          "comment_form": comment_form,
             },
    )

    
class ArtSubmissionList(generic.ListView):
     model = Post
     queryset = Post.objects.filter(status=1).order_by("created_on")
     template_name = "submit_art.html"
     paginate_by = 3 

class SubmitArt(View):
     def get(self, request):
          form = PostForm()
          return render(request, 'submit_art.html', {'form': form})

     def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your Art has been submitted!')
            return redirect('home')
            return render(request, 'submit_art.html', {'form': form})
    