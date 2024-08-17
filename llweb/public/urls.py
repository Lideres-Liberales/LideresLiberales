from django.urls import path
from .views import *

urlpatterns = [
    path(
        route='',
        view=Home.as_view(),
        name='home'
    ),

    # ExecutiveBranch ---------------------------------------------------------
    path(
        route='gabinete',
        view=CabinetView.as_view(),
        name='cabinet'
    ),
    path(
        route='gabinete/<int:pk>',
        view=CabinetDetailView.as_view(),
        name='cabinet_details'
    ),

    # Senator -----------------------------------------------------------------
    path(
        route='senadores',
        view=SenatorView.as_view(),
        name='senator'
    ),
    path(
        route='senadores/<int:pk>',
        view=SenatorDetailView.as_view(),
        name='senator_details'
    ),

    # Deputie -----------------------------------------------------------------
    path(
        route='diputados',
        view=DeputieView.as_view(),
        name='deputie'
    ),
    path(
        route='diputados/<int:pk>',
        view=DeputieDetailView.as_view(),
        name='deputie_details'
    ),

    # CommunityBoard ----------------------------------------------------------
    path(
        route='junta-comunal',
        view=CommunityBoardView.as_view(),
        name='community_board'
    ),
    path(
        route='junta-comunal/<int:pk>',
        view=CommunityBoardDetailView.as_view(),
        name='community_board_details'
    ),

    # Councillor --------------------------------------------------------------
    path(
        route='consejales',
        view=CouncillorView.as_view(),
        name='councillor'
    ),
    path(
        route='consejales/<int:pk>',
        view=CouncillorDetailView.as_view(),
        name='councillor_details'
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