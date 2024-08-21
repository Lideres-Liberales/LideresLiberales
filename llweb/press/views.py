from django.contrib import messages

from django.views.generic.base import TemplateView


class News(TemplateView):
    template_name = 'news.html'
