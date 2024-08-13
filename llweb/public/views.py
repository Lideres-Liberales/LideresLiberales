from collections import defaultdict

from django.contrib import messages

from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Functionary


class Home(TemplateView):
    template_name = 'home.html'


class Cabinet(ListView):
    model = Functionary
    template_name = 'cabinet.html'
    context_object_name = 'functionaries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        functionaries = context['functionaries']
        dic_for_height = defaultdict(list)

        for functionary in functionaries:
            dic_for_height[functionary.height].append(functionary)

        context['functionaries'] = dict(dic_for_height)

        return context


class Official(DetailView):
    model = Functionary

    def render_to_response(self, context, **response_kwargs):
        object_ = context['object']

        html_content = [line.strip() for line in f"""
            <p>{object_.name}</p>
            <p>{object_.position}</p>
            <p>{object_.image}</p>
        """]

        return HttpResponse(html_content, content_type='text/html')


class Join(TemplateView):
    template_name = 'join.html'


class News(TemplateView):
    template_name = 'news.html'


class Events(TemplateView):
    template_name = 'events.html'
