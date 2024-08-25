from django.contrib import messages

from django.views.generic.base import TemplateView

from django.shortcuts import render

class Home(TemplateView):
    template_name = 'home.html'


class Cabinet(TemplateView):
    template_name = 'cabinet.html'


class Join(TemplateView):
    template_name = 'join.html'


class News(TemplateView):
    template_name = 'news.html'


class Events(TemplateView):
    template_name = 'events.html'

# def Calendar(request):
#     eventos = Evento.objects.all()
#     return render(request, 'eventos.html', {'eventos': eventos})
