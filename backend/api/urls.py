from django.urls import path
from . import views
from django.conf import settings



urlpatterns = [
    path('get-list-view', views.NewsListAPIView.as_view(), name='get-list'),
]


if settings.DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True
    settings.INSTALLED_APPS.append(
        'corsheaders'
    )
    settings.MIDDLEWARE.append(
        'corsheaders.middleware.CorsMiddleware',
    )
