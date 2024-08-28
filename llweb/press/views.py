from django.urls import reverse

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import FormView

from .models import Article, Comment
from .forms import CommentForm


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 6

    def get_queryset(self):
        query_order = self.model.objects.order_by('-creation')
        query_related = query_order.select_related('author')

        return query_related


class ArticleView(DetailView, FormView):
    model = Article
    template_name = 'article_details.html'
    context_object_name = 'article'
    form_class = CommentForm
    success_url = 'news-details'

    def get_queryset(self):
        return self.model.objects.select_related('author')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault('form', self.get_form())

        return self.include_comment(context)

    def include_comment(self, context):
        comments = Comment.filter_by_article_id(self.get_pk())
        context['comments'] = comments

        return context

    def form_valid(self, form):
        form.persist(self.get_pk())

        return super().form_valid(form)

    def form_invalid(self, form):
        self.object = self.get_object()

        return super().form_invalid(form)

    def get_success_url(self):
        return reverse(self.success_url, kwargs={'pk': self.get_pk()})

    def get_pk(self):
        return self.kwargs.get(self.pk_url_kwarg)
