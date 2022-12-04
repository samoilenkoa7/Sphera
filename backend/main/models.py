from django.db import models


class NewsModel(models.Model):
    RAITING_CHOICES = (
        (1, 'Like'),
        (-1, 'Dislike')
    )

    title = models.CharField('Title', max_length=255)
    short_description = models.TextField('Short description')
    link = models.TextField('Link on news origin', unique=True)
    raiting = models.IntegerField(choices=RAITING_CHOICES, default=1)
    is_posted = models.BooleanField('Posted?', default=True, db_index=True)
    is_valued = models.BooleanField('Relation to sphere', default=True)
