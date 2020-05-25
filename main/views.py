from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie,Series

# Create your views here.

def index(request):
    return render(request, 'index.html')

def movies(request):
    movies_list = Movie.objects.order_by('point')
    context = {
        'list': movies_list,
    }
    return render(request, 'movies/list.html', context)

def series(request):
    series_list = Series.objects.order_by('point')
    context = {
        'list': series_list,
    }
    return render(request, 'series/list.html', context)