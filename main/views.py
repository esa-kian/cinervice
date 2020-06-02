from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Series, People, Cinema, Role

# Create your views here.

def index(request):
    return render(request, 'index.html')

def movies(request):
    movies_list = Movie.objects.order_by('point')
    context = {
        'list': movies_list,
    }
    return render(request, 'movies/list.html', context)

def movie_info(request):
    pass

def series(request):
    series_list = Series.objects.order_by('point')
    context = {
        'list': series_list,
    }
    return render(request, 'series/list.html', context)

def seri_info(request):
    pass

def peoples(request):
    people_list = People.objects.order_by('point')
    role_list = Role.objects.order_by('person')
    context = {
        'list': people_list,
        'role': role_list,
    }
    return render(request, 'peoples/list.html', context)

def people_info(request):
    pass

def cinemas(request):
    cinema_list = Cinema.objects.order_by('point')
    context = {
        'list': cinema_list
    }
    return render(request, 'cinemas/list.html', context)

def cinema_info(request):
    pass

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')