from django.urls import path
from . import views


urlpatterns = [
    path('get-list-view', views.NewsListAPIView.as_view(), name='get-list'),
]
