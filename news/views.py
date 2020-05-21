from django.shortcuts import render
from django.http import HttpResponse
from .models import New
# Create your views here.

def index(request):
    news_list = New.objects.order_by('title')
    print(news_list)
    context = {
        'news_list': news_list,
    }
    return render(request, 'news.html', context)
    # return HttpResponse("Hello, world. You're at the polls index.")