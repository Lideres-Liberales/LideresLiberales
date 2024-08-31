from django.urls import reverse
from django.db.models import Q
from urllib import parse

from .forms import SearchForm


class SearchBase:
    form_search = SearchForm
    form_action = None
    search_dict = None
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
