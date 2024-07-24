from django.contrib import messages

from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = 'home.html'


class Leaders(TemplateView):
    template_name = 'leaders.html'


class Join(TemplateView):
    template_name = 'join.html'


class News(TemplateView):
    template_name = 'news.html'
