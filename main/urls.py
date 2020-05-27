from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('tv_shows/', views.series, name='series'),
    path('people/', views.peoples, name='peoples'),
    path('movie_theaters/', views.cinemas, name='cinemas'),
]