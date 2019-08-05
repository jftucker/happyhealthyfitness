from django.contrib.auth import get_user_model
from rest_framework import generics

from articles.models import Article
from .permissions import IsAuthorOrReadOnly
from .serializers import ArticleSerializer, UserSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UserList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = UserSerializer