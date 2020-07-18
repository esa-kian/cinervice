from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('movies/<int:movie_id>/', views.movie_info, name='movie_info'),
    path('movies/<int:movie_id>/vote/', views.movie_rate, name='movie_rate'),
    path('tv_shows/', views.series, name='series'),
    path('tv_shows/<int:seri_id>/', views.seri_info, name='seri_info'),
    path('tv_shows/<int:seri_id>/vote/', views.seri_rate, name='seri_rate'),
    path('people/', views.people, name='peoples'),
    path('people/<int:people_id>/', views.people_info, name='people_info'),
    path('people/<int:people_id>/vote/', views.people_rate, name='people_rate'),
    path('movie_theaters/', views.cinemas, name='cinemas'),
    path('movie_theaters/<int:cinema_id>/', views.cinema_info, name='cinema_info'),
    path('movie_theaters/<int:cinema_id>/vote/', views.cinema_rate, name='cinema_rate'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
