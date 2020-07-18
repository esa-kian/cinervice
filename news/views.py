from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import New
# Create your views here.

def index(request):
    news_list = New.objects.all()
    paginator = Paginator(news_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})