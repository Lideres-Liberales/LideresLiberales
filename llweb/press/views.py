from django.urls import reverse
from django.db.models import Q
from urllib import parse

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import FormView

from .models import Article, Comment
from .forms import CommentForm, SearchForm


class RootArticles:
    form_search = SearchForm
    form_action = 'news'
    search_dict = {'query': 'title__contains'}
    page_kwarg = 'page'

    def include_search(self, context, request):
        context['url_params'] = self.url_params()
        context['form_search'] = self.form_search(request.GET)
        context['form_action'] = reverse(self.form_action)

        return context

    def include_filters(self, queryset, request):
        if request.GET:
            search_params = self.search_params(request.GET)
            query_params = self.query_params(search_params)

            return queryset.filter(query_params)

        return queryset

    def url_params(self):
        url_params = parse.urlencode(
            {k: v for k, v in self.request.GET.items() if k != self.page_kwarg}
        )

        return f'?{url_params}&{self.page_kwarg}' if url_params else f'?{self.page_kwarg}'

    def query_params(self, params):
        return Q(**{k: v for k, v in params.items() if v not in (None, '')})

    def search_params(self, params):
        dict_ = self.search_dict
        return {dict_.get(k, k): v for k, v in params.items() if k in dict_}


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
    model = Article
    template_name = 'article_details.html'
    context_object_name = 'article'
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
