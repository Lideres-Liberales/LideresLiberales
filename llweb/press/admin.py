from django.contrib import admin

from .models import Article
from .models import Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'featured_image', 'creation', 'modification')
    search_fields = ('title', 'author', 'featured_image', 'creation', 'modification')
    ordering = ['creation']

    exclude = ('prev_article', 'next_article')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'url', 'message')
    search_fields = ('name', 'email', 'url')
    ordering = ['creation']
