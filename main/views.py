from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import Movie, Series, People, Cinema, Role, Contact_Form, Movies_Vote, Series_Vote, Cinema_Vote, People_Vote
from news.models import New
from django.db.models import Avg

def index(request):
    cinema_in_slider = Cinema.objects.all()[:3]
    news_in_index = New.objects.all()[:5]
    context = {
        'cinema_in_slider': cinema_in_slider,
        'news_in_index': news_in_index,
    }
    return render(request, 'index.html', context)

# Start of Movie Part Methods

def movies(request):
    movie_list = Movie.objects.all()
    paginator = Paginator(movie_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'movies/list.html', {'page_obj': page_obj})

def movie_info(request, movie_id):
    try:    
        movie_info = Movie.objects.filter(pk=movie_id)
        count = Movies_Vote.objects.filter(movie_id=movie_id).count()
        rate = Movies_Vote.objects.filter(movie_id=movie_id).aggregate(Avg('vote')).get('vote__avg')
        if(rate is not None):
            rate = round(rate, 2)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/info.html', { 'info' : movie_info, 'count': count, 'rate': rate })

def movie_rate(request, movie_id):
    if request.method == "GET":
        if(request.user.is_authenticated):
            vote = int(request.GET.get('point'))
            try:
                is_voted = Movies_Vote.objects.get(movie_id=movie_id, user_id=request.user.id)
                if(is_voted is not None):
                    Movies_Vote.objects.filter(movie_id=movie_id, user_id= request.user.id).update(vote=vote)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except:
                if(1<=vote<=10):
                    vote_object = Movies_Vote(vote=vote, movie_id=movie_id , user_id= request.user.id)
                    vote_object.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    return HttpResponse('Your vote is out of range')
        else:
            return HttpResponse('Please Login!')
    else: 
        return HttpResponse('Invalid request')
# End of Movie Part Methods

# Start of TV Shows Part Methods

def series(request):
    series_list = Series.objects.all()
    paginator = Paginator(series_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'series/list.html', {'page_obj': page_obj})

def seri_info(request, seri_id):
    try:    
        seri_info = Series.objects.filter(pk=seri_id)
        count = Series_Vote.objects.filter(serial_id=seri_id).count()
        rate = Series_Vote.objects.filter(serial_id=seri_id).aggregate(Avg('vote')).get('vote__avg')
        if(rate is not None):
            rate = round(rate, 2)
    except Series.DoesNotExist:
        raise Http404("TV Show does not exist")
    return render(request, 'series/info.html', { 'info' : seri_info, 'count': count, 'rate': rate })

def seri_rate(request, seri_id):
    if request.method == "GET":
        if(request.user.is_authenticated):
            vote = int(request.GET.get('point'))
            try:
                is_voted = Series_Vote.objects.get(serial_id=seri_id, user_id=request.user.id)
                if(is_voted is not None):
                    Series_Vote.objects.filter(serial_id=seri_id, user_id= request.user.id).update(vote=vote)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except:
                if(1<=vote<=10):
                    vote_object = Series_Vote(vote=vote, serial_id=seri_id , user_id= request.user.id)
                    vote_object.save()

                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    return HttpResponse('Your vote is out of range')
        else:
            return HttpResponse('Please Login!')
    else: 
        return HttpResponse('Invalid request')

# End of TV Shows Part Methods

# Start of Celebrity Part Methods

def people(request):
    people_list = People.objects.all()
    paginator = Paginator(people_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'peoples/list.html', context)

def people_info(request, people_id):
    try:    
        people_info = People.objects.filter(pk=people_id)
        count = People_Vote.objects.filter(people_id=people_id).count()
        rate = People_Vote.objects.filter(people_id=people_id).aggregate(Avg('vote')).get('vote__avg')
        if(rate is not None):
            rate = round(rate, 2)
        role_list = Role.objects.all().filter(person_id=people_id)
        context = {
            'info': people_info,
            'role': role_list,
            'count': count,
            'rate': rate,
        }
    except People.DoesNotExist:
        raise Http404("People does not exist")
    return render(request, 'peoples/info.html', context)

def people_rate(request, people_id):
    if request.method == "GET":
        if(request.user.is_authenticated):
            vote = int(request.GET.get('point'))
            try:
                is_voted = People_Vote.objects.get(people_id=people_id, user_id=request.user.id)
                if(is_voted is not None):
                    People_Vote.objects.filter(people_id=people_id, user_id= request.user.id).update(vote=vote)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except:
                if(1<=vote<=10):
                    vote_object = People_Vote(vote=vote, people_id=people_id , user_id= request.user.id)
                    vote_object.save()

                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    return HttpResponse('Your vote is out of range')
        else:
            return HttpResponse('Please Login!')
    else: 
        return HttpResponse('Invalid request')

# End of Celebrity Part Methods

# Start of Movie Theater Part Methods

def cinemas(request):
    cinema_list = Cinema.objects.all()
    paginator = Paginator(cinema_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'cinemas/list.html', context)

def cinema_info(request, cinema_id):
    try:    
        cinema_info = Cinema.objects.filter(pk=cinema_id)
        count = Cinema_Vote.objects.filter(cinema_id=cinema_id).count()
        rate = Cinema_Vote.objects.filter(cinema_id=cinema_id).aggregate(Avg('vote')).get('vote__avg')
        if(rate is not None):
            rate = round(rate, 2)
    except Cinema.DoesNotExist:
        raise Http404("Movie Theater does not exist")
    return render(request, 'cinemas/info.html', {'info': cinema_info, 'count': count, 'rate': rate })

def cinema_rate(request, cinema_id):
    if request.method == "GET":
        if(request.user.is_authenticated):
            vote = int(request.GET.get('point'))
            try:
                is_voted = Cinema_Vote.objects.get(cinema_id=cinema_id, user_id=request.user.id)
                if(is_voted is not None):
                    Cinema_Vote.objects.filter(cinema_id=cinema_id, user_id= request.user.id).update(vote=vote)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except:
                if(1<=vote<=10):
                    vote_object = Cinema_Vote(vote=vote, cinema_id=cinema_id , user_id= request.user.id)
                    vote_object.save()

                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    return HttpResponse('Your vote is out of range')
        else:
            return HttpResponse('Please Login!')
    else: 
        return HttpResponse('Invalid request')
# End of Movie Theater Part Methods

# About Part Method
def about(request):
    return render(request, 'about.html')

# Contact Part Method
def contact(request):
    if request.method == "GET":
        return render(request, 'contact.html')
    elif request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact_form = Contact_Form(first_name = first_name, last_name = last_name, email = email, subject = subject)
        contact_form.save()
        return JsonResponse({'situation':'Your form has been received!'})
    else:
        return JsonResponse({'situation':'Invalid request!'})