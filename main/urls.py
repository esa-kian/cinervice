from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('tv_shows/', views.series, name='series'),
    path('peoples/', views.peoples, name='peoples'),
    path('movie_theater', views.cinemas, name='cinemas'),
]