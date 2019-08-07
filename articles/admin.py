from django.contrib import admin
from django import forms

from .models import Article, Comment

from ckeditor.widgets import CKEditorWidget


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = '__all__'
    
class ArticleAdmin(admin.ModelAdmin):
    
    form = ArticleAdminForm
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)