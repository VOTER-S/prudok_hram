from django.shortcuts import render
from .models import News, Schedule# Импортируем модель News
from django.shortcuts import  get_object_or_404
def index(request):
    schedule = Schedule.objects.all()  # Берём все карточки из базы
    return render(request, 'kirks/index.html',  {'schedule': schedule})


def news_list(request):
    news_list = News.objects.all()
    return render(request, 'kirks/news_list.html', {'news_list': news_list})

def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    return render(request, 'kirks/news_detail.html', {'news_item': news_item})



def build(request):
    return render(request, 'kirks/build.html')