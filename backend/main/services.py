from django.db import IntegrityError
from requests_html import HTMLSession

from .models import NewsModel


def check_news_and_add():
    session = HTMLSession()

    url = 'https://www.sciencedaily.com/rss/mind_brain.xml'

    r = session.get(url)
    news = r.html.find('item')
    print(news)
    for new in news:
        for i in new.find('title'):
            title = i.text
        for i in new.find('description'):
            description = i.text
        for i in new.find('guid'):
            link = i.text
        try:
            NewsModel.objects.create(title=title, short_description=description, link=link)
        except IntegrityError as ex:
            print(ex)
            break


def calc_color(negative_votes: int, postitive_votes: int) -> tuple:
    """
    Args:
        negative_votes (int): number of positve votes
        postitive_votes (int): number of negative votes
    Returns:
        tuple: tuple of ints corresponding an rgb
    """
    satisfied_res = postitive_votes / (negative_votes + postitive_votes)
    rgb_eq = int(satisfied_res * 255)
    return (rgb_eq, rgb_eq, rgb_eq)
