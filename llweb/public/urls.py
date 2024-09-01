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
        route='eventos',
        view=Events.as_view(),
        name='events'
    ),
]
