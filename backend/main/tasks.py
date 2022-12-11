from celery import shared_task

from main.models import NewsModel
from main.services import check_news_and_add
from sphera.celery import app


@shared_task
def parse_news_website():
    check_news_and_add()
