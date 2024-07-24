from django.urls import path
from .views import *

urlpatterns = [
    path(
        route='',
        view=Home.as_view(),
        name='home'
    ),
    path(
        route='lideres-liberales',
        view=Leaders.as_view(),
        name='leaders'
    ),
    path(
        route='sumate',
        view=Join.as_view(),
        name='join'
    ),
    path(
        route='novedades',
        view=News.as_view(),
        name='news'
    ),
]