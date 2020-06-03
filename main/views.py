from django.shortcuts import render
from django.http import HttpResponse, Http404
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

def movie_info(request, movie_id):
    try:    
        movie_info = Movie.objects.filter(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/info.html', { 'info' : movie_info})

def series(request):
    series_list = Series.objects.order_by('point')
    context = {
        'list': series_list,
    }
    return render(request, 'series/list.html', context)

def seri_info(request, seri_id):
    try:    
        seri_info = Series.objects.filter(pk=seri_id)
    except Series.DoesNotExist:
        raise Http404("TV Show does not exist")
    return render(request, 'series/info.html', { 'info' : seri_info})

def peoples(request):
    people_list = People.objects.order_by('point')
    role_list = Role.objects.order_by('person')
    context = {
        'list': people_list,
        'role': role_list,
    }
    return render(request, 'peoples/list.html', context)

def people_info(request, people_id):
    try:    
        people_info = People.objects.filter(pk=people_id)
        role_list = Role.objects.order_by('person')
        context = {
            'info': people_info,
            'role': role_list,
        }
    except People.DoesNotExist:
        raise Http404("People does not exist")
    return render(request, 'peoples/info.html', context)

def cinemas(request):
    cinema_list = Cinema.objects.order_by('point')
    context = {
        'list': cinema_list
    }
    return render(request, 'cinemas/list.html', context)

def cinema_info(request, cinema_id):
    try:    
        cinema_info = Cinema.objects.filter(pk=cinema_id)
    except Cinema.DoesNotExist:
        raise Http404("Movie Theater does not exist")
    return render(request, 'cinemas/info.html', {'info': cinema_info})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')