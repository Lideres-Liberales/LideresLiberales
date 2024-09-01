from django import template
from markdown import Markdown

from root.parser import LlwebExtension

register = template.Library()
markdown = Markdown(extensions=[LlwebExtension()])


@register.filter(name='markdown_to_html')
def markdown_to_html(value):
    return markdown.convert(value) if value is not None else ''
