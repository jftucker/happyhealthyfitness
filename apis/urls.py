from django.urls import path

from .views import ArticleList, ArticleDetail, UserList, UserDetail

from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'Happy Healthy Fitness API'
API_DESCRIPTION = 'A Web API to interact with happyhealthy.fitness'

schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('articles/<int:pk>/', ArticleDetail.as_view()),
    path('articles/', ArticleList.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('', schema_view),
]