from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.

def index(request):
    return render(request, 'index.html')

def movies(request):
    best_movies_list = Movie.objects.order_by('point')
    print(best_movies_list)
    context = {
        'list': best_movies_list,
    }
    return render(request, 'movies/list.html', context)