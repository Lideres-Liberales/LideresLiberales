from django.urls import path
from .views import *

urlpatterns = [
    path(
        route='sumate',
        view=Join.as_view(),
        name='join'
    ),
]
