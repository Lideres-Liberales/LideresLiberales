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


class FunctionaryMixin:
    template_name = 'functionary.html'
    context_object_name = 'functionaries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['politicalsParties'] = self.get_references()

        return context

    def get_references(self):
        return PoliticalParty.objects.filter(**{
            self.get_related_name_party() + '__isnull': False
        }).distinct()

    def get_related_name_party(self):
        return self.model.__name__.lower() + '_political_party'


class CabinetView(FunctionaryMixin, ListView):
    model = ExecutiveBranch

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['functionaries'] = self.list_to_dict(context['functionaries'])

        return context

    def list_to_dict(self, functionaries_list):
        dic_for_height = defaultdict(list)

        for functionary in functionaries_list:
            dic_for_height[functionary.height].append(functionary)

        return dict(dic_for_height)


class SenatorView(FunctionaryMixin, ListView):
    model = Senator


class DeputieView(FunctionaryMixin, ListView):
    model = Deputie


class CommunityBoardView(FunctionaryMixin, ListView):
    model = CommunityBoard


class CouncillorView(FunctionaryMixin, ListView):
    model = Councillor


# -----------------------------------------------------------------------------
class FunctionaryDetailMixin:
    template_name = 'functionary-detail.html'
    context_object_name = 'functionary'


class CabinetDetailView(FunctionaryDetailMixin, DetailView):
    model = ExecutiveBranch


class SenatorDetailView(FunctionaryDetailMixin, DetailView):
    model = Senator


class DeputieDetailView(FunctionaryDetailMixin, DetailView):
    model = Deputie


class CommunityBoardDetailView(FunctionaryDetailMixin, DetailView):
    model = CommunityBoard


class CouncillorDetailView(FunctionaryDetailMixin, DetailView):
    model = Councillor


# -----------------------------------------------------------------------------
class Join(TemplateView):
    template_name = 'join.html'


class News(TemplateView):
    template_name = 'news.html'


class Events(TemplateView):
    template_name = 'events.html'
