from collections import defaultdict

from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Functionary
from .models import PoliticalParty


class Home(TemplateView):
    template_name = 'home.html'


class Cabinet(ListView):
    model = Functionary
    template_name = 'cabinet.html'
    context_object_name = 'functionaries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['functionaries'] = self.list_to_dict(context['functionaries'])
        context['politicalsParties'] = self.get_references()

        return context

    def list_to_dict(self, functionaries_list):
        dic_for_height = defaultdict(list)

        for functionary in functionaries_list:
            dic_for_height[functionary.height].append(functionary)

        return dict(dic_for_height)

    def get_references(self):
        return PoliticalParty.objects.filter(political_party__isnull=False).distinct()


class FunctionaryDetail(DetailView):
    model = Functionary
    template_name = 'functionary-detail.html'
    context_object_name = 'functionary'


class Join(TemplateView):
    template_name = 'join.html'


class News(TemplateView):
    template_name = 'news.html'


class Events(TemplateView):
    template_name = 'events.html'
