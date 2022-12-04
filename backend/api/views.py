from rest_framework import generics
from main.models import NewsModel
from .serializers import NewsModelSerializer


class NewsListAPIView(generics.ListAPIView):
    serializer_class = NewsModelSerializer

    def get_queryset(self):
        return NewsModel.objects.filter(is_posted=True, is_valued=True)
