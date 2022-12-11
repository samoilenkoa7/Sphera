from django.db.models import Count
from django.shortcuts import render
from .services import check_news_and_add, calc_color
from .tasks import create_new_post

from .models import NewsModel


def main_page(request):
    news = NewsModel.objects.all()
    data = {}
    data['news'] = news
    likes = NewsModel.objects.filter(raiting=1).count()
    dislikes = NewsModel.objects.filter(raiting=-1).count()
    data['color'] = calc_color(postitive_votes=likes, negative_votes=dislikes)
    return render(request, template_name='main/main-page.html', context=data)