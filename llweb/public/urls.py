from django.urls import path
from .views import *

urlpatterns = [
    path(
        route='',
        view=Home.as_view(),
        name='home'
    ),
    path(
        route='gabinete',
        view=Cabinet.as_view(),
        name='cabinet'
    ),
    path(
        route='gabinete/<int:pk>',
        view=FunctionaryDetail.as_view(),
        name='public_official'
    ),
    path(
        route='sumate',
        view=Join.as_view(),
        name='join'
    ),
    path(
        route='prensa',
        view=News.as_view(),
        name='news'
    ),
    path(
        route='eventos',
        view=Events.as_view(),
        name='events'
    ),
]