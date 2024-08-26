from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.shortcuts import render
from users.models import Evento

class Home(TemplateView):
    template_name = 'home.html'


class Cabinet(TemplateView):
    template_name = 'cabinet.html'


class Join(TemplateView):
    template_name = 'join.html'


class News(TemplateView):
    template_name = 'news.html'

class Calendar(ListView):
    model = Evento
    template_name = 'events.html'
    context_object_name = 'eventos'