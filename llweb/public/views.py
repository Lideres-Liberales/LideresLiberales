from django.contrib import messages

from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import DetailView

from .models import Functionary


class Home(TemplateView):
    template_name = 'home.html'


class Cabinet(DetailView):
    template_name = 'cabinet.html'
    context_object_name = 'principal'
    model = Functionary

    def get_object(self, queryset=None):
        try:
            objeto_ = Functionary.objects.get(position="CEO")
        except Functionary.DoesNotExist:
            objeto_ = None

        return objeto_


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
