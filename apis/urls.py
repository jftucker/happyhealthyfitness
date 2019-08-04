from django.urls import path

from .views import ArticleList, ArticleDetail

urlpatterns = [
    path('articles/<int:pk>/', ArticleDetail.as_view()),
    path('articles/', ArticleList.as_view()),
]