from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(config_name='default')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    link = models.CharField(max_length=255, null=True, blank=True)
    link_text = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')


class Image(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='images',
    )
    title = models.CharField(max_length=140, null=True, blank=True)
    image = models.ImageField('image', upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.image.url

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])