from django.urls import path
from .views import *

urlpatterns = [
    path(
        route='prensa',
        view=ArticleListView.as_view(),
        name='news'
    ),
]
