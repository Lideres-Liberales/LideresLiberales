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
        route='valores',
        view=Ethics.as_view(),
        name='ethics'
    ),
    path(
        route='eventos',
        view=Events.as_view(),
        name='events'
    ),
]