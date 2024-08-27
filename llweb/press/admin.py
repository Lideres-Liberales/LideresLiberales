from django.contrib import admin
from django import forms

from .widgets import Wysiwyg
from .models import Article
from .models import Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ('prev_article', 'next_article')
        widgets = {'body': Wysiwyg()}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'featured_image', 'creation', 'modification')
    search_fields = ('title', 'author', 'featured_image', 'creation', 'modification')
    ordering = ['-creation']

    form = ArticleForm
    change_form_template = 'admin/article_form_admin.html'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'url', 'message')
    search_fields = ('name', 'email', 'url')
    ordering = ['-creation']
