from django.urls import path
from .views import *

urlpatterns = [
    path(
        route='prensa',
        view=ArticleListView.as_view(),
        name='news'
    ),
    path(
        route='prensa/<int:pk>',
        view=ArticleView.as_view(),
        name='news-details'
    ),
]
