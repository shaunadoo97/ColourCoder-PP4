from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.
class ArtPostList(generic.ListView):
     queryset = Post.objects.all()
     template_name = "artblog/artindex.html"
     paginate_by = 6