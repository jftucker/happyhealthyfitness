from django.contrib.auth import get_user_model
from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Article


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)