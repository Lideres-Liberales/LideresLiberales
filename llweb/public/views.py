from abc import ABC
from collections import defaultdict

from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import PoliticalParty
from .models import ExecutiveBranch
from .models import Senator
from .models import Deputie
from .models import CommunityBoard
from .models import Councillor


class Home(TemplateView):
    template_name = 'home.html'


# -----------------------------------------------------------------------------
class FunctionaryView(ListView, ABC):
    template_name = 'functionary.html'
    context_object_name = 'functionaries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        functionaries = context['functionaries']

        context['functionaries'] = self.list_to_dict(functionaries)
        context['politicalsParties'] = self.get_references(functionaries)

        return context

    def get_queryset(self):
        return self.model.objects.select_related('political_party').all()

    def list_to_dict(self, functionaries):
        return {'0': functionaries}

    def get_references(self, functionaries):
        return {functionary.political_party for functionary in functionaries}


class CabinetView(FunctionaryView):
    model = ExecutiveBranch

    def list_to_dict(self, functionaries):
        dic_for_height = defaultdict(list)

        for functionary in functionaries:
            dic_for_height[functionary.height].append(functionary)

        return dict(dic_for_height)


class SenatorView(FunctionaryView):
    model = Senator


class DeputieView(FunctionaryView):
    model = Deputie


class CommunityBoardView(FunctionaryView):
    model = CommunityBoard


class CouncillorView(FunctionaryView):
    model = Councillor


# -----------------------------------------------------------------------------
class FunctionaryDetailView(DetailView, ABC):
    template_name = 'functionary-detail.html'
    context_object_name = 'functionary'


class CabinetDetailView(FunctionaryDetailView):
    model = ExecutiveBranch


class SenatorDetailView(FunctionaryDetailView):
    model = Senator


class DeputieDetailView(FunctionaryDetailView):
    model = Deputie


class CommunityBoardDetailView(FunctionaryDetailView):
    model = CommunityBoard


class CouncillorDetailView(FunctionaryDetailView):
    model = Councillor


# -----------------------------------------------------------------------------
class Join(TemplateView):
    template_name = 'join.html'


class News(TemplateView):
    template_name = 'news.html'


class Events(TemplateView):
    template_name = 'events.html'
