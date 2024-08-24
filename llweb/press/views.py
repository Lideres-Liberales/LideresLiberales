from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Article
from .forms import CommentForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()

        return context
