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


class Evento(TemplateView):
    template_name = 'events.html'
    
def calendario(request):
    events = Evento.objects.all()
    context = {
        'eventos': events
    }
    return render(request, 'events.html', context)