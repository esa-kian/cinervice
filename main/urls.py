from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('movies/<int:movie_id>/', views.movie_info, name='movie_info'),
    path('tv_shows/', views.series, name='series'),
    path('tv_shows/<int:seri_id>/', views.seri_info, name='seri_info'),
    path('people/', views.peoples, name='peoples'),
    path('people/<int:people_id>/', views.people_info, name='people_info'),
    path('movie_theaters/', views.cinemas, name='cinemas'),
    path('movie_theaters/<int:cinema_id>/', views.cinema_info, name='cinema_info'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]