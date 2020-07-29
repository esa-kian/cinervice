from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import Movie, Series, People, Cinema, Role, Contact_Form, Movies_Vote, Series_Vote, Cinema_Vote, People_Vote
from news.models import New
from django.db.models import Avg, Count
from itertools import chain


def index(request):
    if(request.user.is_authenticated):
        # Estimate average of user votes
        rate_avg_movie = Movies_Vote.objects.filter(
            user_id=request.user.id).aggregate(Avg('vote')).get('vote__avg')
        rate_avg_serial = Series_Vote.objects.filter(
            user_id=request.user.id).aggregate(Avg('vote')).get('vote__avg')
        rate_avg_people = People_Vote.objects.filter(
            user_id=request.user.id).aggregate(Avg('vote')).get('vote__avg')
        rate_avg_cinema = Cinema_Vote.objects.filter(
            user_id=request.user.id).aggregate(Avg('vote')).get('vote__avg')

        if(rate_avg_movie is not None or rate_avg_serial is not None or
           rate_avg_people is not None or rate_avg_cinema is not None):
            if(rate_avg_movie is None):
                rate_avg_movie = 0
            if(rate_avg_serial is None):
                rate_avg_serial = 0
            if(rate_avg_people is None):
                rate_avg_people = 0
            if(rate_avg_cinema is None):
                rate_avg_cinema = 0
            avg_vote = (rate_avg_movie+rate_avg_serial +
                        rate_avg_people+rate_avg_cinema)/4

            # Suggest By Vote to The People
            cinema_in_slider_by_people = []

            # fetch all popular people
            all_fav_people = People_Vote.objects.filter(
                vote__gte=avg_vote, user_id=request.user.id)

            for i in all_fav_people:
                # fetch all role of popular people
                all_role_of_fav_people = Role.objects.filter(
                    person=i.people_id)

                for ii in all_role_of_fav_people:
                    # filter popular movie of popular people
                    fav_movie_filtered = Movies_Vote.objects.filter(
                        movie=ii.movie_id, user_id=request.user.id).exclude(vote__lt=rate_avg_movie)

                    for iii in fav_movie_filtered:
                        # fetch all role in popular movie
                        all_role_in_fav_movie = Role.objects.filter(
                            movie=iii.movie_id)
                        sum_rate_of_people_in_movie = 0

                        for calc in all_role_in_fav_movie:
                            # calculate average rate of popular movie
                            sum_rate_of_people_in_movie += People_Vote.objects.filter(people=calc.person_id,
                                                                                      user_id=request.user.id).aggregate(Avg('vote')).get('vote__avg')
                        avg_rate_of_people_in_movie = sum_rate_of_people_in_movie / \
                            all_role_in_fav_movie.count()
                        if avg_rate_of_people_in_movie >= rate_avg_people:
                            for iv in all_role_in_fav_movie:
                                cinema_by_filtered_movie = Cinema.objects.filter(
                                    movie=iv.movie_id)

                                for v in cinema_by_filtered_movie:
                                    fav_cinema = Cinema_Vote.objects.filter(
                                        user_id=request.user.id, cinema=v.id).exclude(vote__lt=rate_avg_cinema)

                                    for vi in fav_cinema:
                                        filtered_cinema = Cinema.objects.filter(
                                            id=vi.cinema_id)
                                        cinema_in_slider_by_people = list(
                                            chain(filtered_cinema))

            # Suggest By Vote to The Movie(people are same)
            cinema_in_slider_by_movie = []

            # fetch all popular movie
            all_fav_movie = Movies_Vote.objects.filter(
                vote__gte=avg_vote, user_id=request.user.id)

            for i in all_fav_movie:
                # fetch all role in popular movie
                all_role_in_fav_movie = Role.objects.filter(movie=i.movie_id)
                for ii in all_role_in_fav_movie:
                    # filter popular people in movie(make function <filter_popular_people> for this!!!!!!!)
                    fav_people_in_movie = People_Vote.objects.filter(
                        people=ii.person_id, user_id=request.user.id).exclude(vote__lt=rate_avg_people)
                    for iii in fav_people_in_movie:
                        # fetch popular people(make function <fetch_popular_people> for this!!!!!!!)
                        fetch_popular_people = Role.objects.filter(
                            person=iii.people_id)

                        for iv in fetch_popular_people:
                            # fetch movies of popular people(make function <fetch_movie_of_popular_people> for this!!!!!)
                            movies_of_popular_people = Movie.objects.filter(
                                id=iv.movie_id)
                            for v in movies_of_popular_people:
                                # filter popular movies of people
                                fav_movie_filtered = Movies_Vote.objects.filter(
                                    movie=v.id, user_id=request.user.id).exclude(vote__lt=rate_avg_movie)
                                for vi in fav_movie_filtered:
                                    # fetch cinemas have popular movie
                                    find_cinema_for_fav_movie = Cinema.objects.filter(
                                        movie=vi.movie_id)
                                    for vii in find_cinema_for_fav_movie:
                                        # filter popular cinema of movie
                                        fav_cinema_filtered = Cinema_Vote.objects.filter(
                                            cinema=vii.id, user_id=request.user.id).exclude(vote__lt=rate_avg_cinema)
                                        for it in fav_cinema_filtered:
                                            cinema_in_slider_by_movie = Cinema.objects.filter(
                                                id=it.cinema_id)

            # Suggest By Vote to The Serial(people are same)
            cinema_in_slider_by_serial = []

            # fetch all popular serial
            all_fav_serial = Series_Vote.objects.filter(
                vote__gte=avg_vote, user_id=request.user.id)

            for i in all_fav_serial:
                # fetch all role in popular serial
                all_role_in_fav_serial = Role.objects.filter(
                    serial=i.serial_id)

                for ii in all_role_in_fav_serial:
                    # filter popular people in serial(make function <filter_popular_people> for this!!!!!!!)
                    fav_people_in_serial = People_Vote.objects.filter(
                        people=ii.person_id, user_id=request.user.id).exclude(vote__lt=rate_avg_people)

                    for iii in fav_people_in_serial:
                        # fetch popular people(make function <fetch_popular_people> for this!!!!!!!)
                        fetch_popular_people = Role.objects.filter(
                            person=iii.people_id)

                        for iv in fetch_popular_people:
                            # fetch movies of popular people(make function <fetch_movie_of_popular_people> for this!!!!!)
                            movies_of_popular_people = Movie.objects.filter(
                                id=iv.movie_id)

                            for v in movies_of_popular_people:
                                # filter popular movies of people
                                fav_movie_filtered = Movies_Vote.objects.filter(
                                    movie=v.id, user_id=request.user.id).exclude(vote__lt=rate_avg_movie)

                                for vi in fav_movie_filtered:
                                    # fetch cinemas have popular movie
                                    find_cinema_for_fav_movie = Cinema.objects.filter(
                                        movie=vi.movie_id)

                                    for vii in find_cinema_for_fav_movie:
                                        # filter popular cinema of movie
                                        fav_cinema_filtered = Cinema_Vote.objects.filter(
                                            cinema=vii.id, user_id=request.user.id).exclude(vote__lt=rate_avg_cinema)

                                        for it in fav_cinema_filtered:
                                            cinema_in_slider_by_serial = Cinema.objects.filter(
                                                id=it.cinema_id)

            cinema_in_slider = list(chain(
                cinema_in_slider_by_movie, cinema_in_slider_by_people, cinema_in_slider_by_serial))
            print(cinema_in_slider)

        else:
            cinema_in_slider = Cinema.objects.all()[:3]

    # NONE Suggestion
    else:
        cinema_in_slider = Cinema.objects.all()[:3]

    news_in_index = New.objects.all()[:5]
    context = {
        'cinema_in_slider': cinema_in_slider,
        'news_in_index': news_in_index,
    }
    # print(cinema_in_slider)
    return render(request, 'index.html', context)

# Start of Movie Part Methods


def movies(request):
    movie_list = Movie.objects.all()
    paginator = Paginator(movie_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'movies/list.html', {'page_obj': page_obj})


def movie_info(request, movie_id):
    try:
        movie_info = Movie.objects.filter(pk=movie_id)
        count = Movies_Vote.objects.filter(movie_id=movie_id).count()
        rate = Movies_Vote.objects.filter(
            movie_id=movie_id).aggregate(Avg('vote')).get('vote__avg')
        if(rate is not None):
            rate = round(rate, 2)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/info.html', {'info': movie_info, 'count': count, 'rate': rate})


def movie_rate(request):
    if request.method == "POST":
        if(request.user.is_authenticated):
            vote = int(request.POST.get('point'))
            try:
                is_voted = Movies_Vote.objects.get(
                    movie_id=request.POST.get('movie-id'), user_id=request.user.id)
                if(is_voted is not None):
                    if(1 > vote or vote > 10):
                        return HttpResponse('Your vote is out of range')
                    else:
                        Movies_Vote.objects.filter(movie_id=request.POST.get(
                            'movie-id'), user_id=request.user.id).update(vote=vote)
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except:
                if(1 > vote or vote > 10):
                    return HttpResponse('Your vote is out of range')
                else:
                    vote_object = Movies_Vote(vote=vote, movie_id=request.POST.get(
                        'movie-id'), user_id=request.user.id)
                    vote_object.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponse('Please Login!')
    else:
        return HttpResponse('Invalid request')
# End of Movie Part Methods

# Start of TV Shows Part Methods


def series(request):
    series_list = Series.objects.all()
    paginator = Paginator(series_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'series/list.html', {'page_obj': page_obj})


def seri_info(request, seri_id):
    try:
        seri_info = Series.objects.filter(pk=seri_id)
        count = Series_Vote.objects.filter(serial_id=seri_id).count()
        rate = Series_Vote.objects.filter(
            serial_id=seri_id).aggregate(Avg('vote')).get('vote__avg')
        if(rate is not None):
            rate = round(rate, 2)
    except Series.DoesNotExist:
        raise Http404("TV Show does not exist")
    return render(request, 'series/info.html', {'info': seri_info, 'count': count, 'rate': rate})


def seri_rate(request):
    if request.method == "POST":
        if(request.user.is_authenticated):
            vote = int(request.POST.get('point'))
            try:
                is_voted = Series_Vote.objects.get(
                    serial_id=request.POST.get('serial-id'), user_id=request.user.id)
                if(is_voted is not None):
                    if(1 > vote or vote > 10):
                        return HttpResponse('Your vote is out of range')
                    else:
                        Series_Vote.objects.filter(serial_id=request.POST.get(
                            'serial-id'), user_id=request.user.id).update(vote=vote)
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except:
                if(1 > vote or vote > 10):
                    return HttpResponse('Your vote is out of range')
                else:
                    vote_object = Series_Vote(vote=vote, serial_id=request.POST.get(
                        'serial-id'), user_id=request.user.id)
                    vote_object.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponse('Please Login!')
    else:
        return HttpResponse('Invalid request')

# End of TV Shows Part Methods

# Start of Celebrity Part Methods


def people(request):
    people_list = People.objects.all()
    paginator = Paginator(people_list, 3)
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
        rate = People_Vote.objects.filter(
            people_id=people_id).aggregate(Avg('vote')).get('vote__avg')
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


def people_rate(request):
    if request.method == "POST":
        if(request.user.is_authenticated):
            vote = int(request.POST.get('point'))
            try:
                is_voted = People_Vote.objects.get(
                    people_id=request.POST.get('people-id'), user_id=request.user.id)
                if(is_voted is not None):
                    if(1 > vote or vote > 10):
                        return HttpResponse('Your vote is out of range')
                    else:
                        People_Vote.objects.filter(people_id=request.POST.get(
                            'people-id'), user_id=request.user.id).update(vote=vote)
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            except:
                if(1 > vote or vote > 10):
                    return HttpResponse('Your vote is out of range')
                else:
                    vote_object = People_Vote(vote=vote, people_id=request.POST.get(
                        'people-id'), user_id=request.user.id)
                    vote_object.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponse('Please Login!')
    else:
        return HttpResponse('Invalid request')

# End of Celebrity Part Methods

# Start of Movie Theater Part Methods


def cinemas(request):
    cinema_list = Cinema.objects.all()
    paginator = Paginator(cinema_list, 1)
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
        rate = Cinema_Vote.objects.filter(
            cinema_id=cinema_id).aggregate(Avg('vote')).get('vote__avg')
        if(rate is not None):
            rate = round(rate, 2)
    except Cinema.DoesNotExist:
        raise Http404("Movie Theater does not exist")
    return render(request, 'cinemas/info.html', {'info': cinema_info, 'count': count, 'rate': rate})


def cinema_rate(request):
    if request.method == "POST":
        if(request.user.is_authenticated):
            vote = int(request.POST.get('point'))
            try:
                is_voted = Cinema_Vote.objects.get(
                    cinema_id=request.POST.get('cinema-id'), user_id=request.user.id)
                if(is_voted is not None):
                    if(1 > vote or vote > 10):
                        return HttpResponse('Your vote is out of range')
                    else:
                        Cinema_Vote.objects.filter(cinema_id=request.POST.get(
                            'cinema-id'), user_id=request.user.id).update(vote=vote)
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except:
                if(1 > vote or vote > 10):
                    return HttpResponse('Your vote is out of range')
                else:
                    vote_object = Cinema_Vote(vote=vote, cinema_id=request.POST.get(
                        'cinema-id'), user_id=request.user.id)
                    vote_object.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
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
        contact_form = Contact_Form(
            first_name=first_name, last_name=last_name, email=email, subject=subject)
        contact_form.save()
        return JsonResponse({'situation': 'Your form has been received!'})
    else:
        return JsonResponse({'situation': 'Invalid request!'})
