from django.urls import path

from .views import HomePageView, EbookPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('downloads/ebook/', EbookPageView.as_view(), name='ebook')
]