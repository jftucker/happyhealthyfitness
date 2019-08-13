from django.contrib import admin
from django import forms

from .models import Article, Comment, Image

from ckeditor.widgets import CKEditorWidget


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

class ArticleAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = '__all__'
    
class ArticleAdmin(admin.ModelAdmin):
    
    form = ArticleAdminForm
    inlines = [
        ImageInline,
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)