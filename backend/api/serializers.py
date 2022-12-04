from rest_framework.serializers import ModelSerializer
from main.models import NewsModel


class NewsModelSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = "__all__"
