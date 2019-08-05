from django.urls import path

from .views import ArticleList, ArticleDetail, UserList, UserDetail

urlpatterns = [
    path('articles/<int:pk>/', ArticleDetail.as_view()),
    path('articles/', ArticleList.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]