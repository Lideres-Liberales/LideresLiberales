from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView


class Home(TemplateView):
    template_name = 'home.html'


class Cabinet(TemplateView):
    template_name = 'cabinet.html'


class Events(TemplateView):
    template_name = 'events.html'
