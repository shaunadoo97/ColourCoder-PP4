from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_artblog(request):
    return HttpResponse("Hello Art!")