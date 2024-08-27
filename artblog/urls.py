from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArtPostList.as_view(), name='home'),
    path('<slug:slug>/', views.artpost_detail, name='artpost_detail'),
]  