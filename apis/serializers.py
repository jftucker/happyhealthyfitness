from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Article