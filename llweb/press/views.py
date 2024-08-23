from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 6

    def get_queryset(self):
        return self.model.objects.select_related('author')


class ArticleView(DetailView):
    model = Article
    template_name = 'article_details.html'
    context_object_name = 'article'

    def get_queryset(self):
        return self.model.objects.select_related('author')