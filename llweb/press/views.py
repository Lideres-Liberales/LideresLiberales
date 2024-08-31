from django.urls import reverse

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import FormView

from root.views import SearchBase

from .models import Article
from .models import Comment
from .forms import CommentForm


class RootArticles(SearchBase):
    form_action = 'news'
    search_dict = {'query': 'title__contains'}


class ArticleListView(RootArticles, ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 6

    def get_queryset(self):
        query_order = self.model.objects.order_by('-creation')
        query_related = query_order.select_related('author')
        queryset = self.include_filters(query_related, self.request)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.include_search(context, self.request)

        return context


class ArticleView(RootArticles, DetailView, FormView):
    # detail view
    model = Article
    template_name = 'article_details.html'
    context_object_name = 'article'

    # form view
    form_class = CommentForm
    success_url = 'news-details'

    def get_queryset(self):
        return self.model.objects.select_related('author')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.include_search(context, self.request)
        context = self.include_comment(context)
        context = self.include_form_comment(context)

        return self.include_comment(context)

    def include_form_comment(self, context):
        context['form'] = self.get_form()

        return context

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
