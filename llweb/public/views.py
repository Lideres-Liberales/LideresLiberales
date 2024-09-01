from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = 'home.html'


class Cabinet(TemplateView):
    template_name = 'cabinet.html'


class Events(TemplateView):
    template_name = 'events.html'
    context_object_name = 'eventos'