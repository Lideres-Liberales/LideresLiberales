import markdown

from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
import xml.etree.ElementTree as etree

import re

class CustomInlineProcessor(InlineProcessor):
    def __init__(self, pattern, markdown, t_node, class_='', style_=''):
        super().__init__(pattern, markdown)

        self.t_node = t_node
        self.class_ = class_
        self.style_ = style_
    
    def handleMatch(self, m, data):
        el = etree.Element(self.t_node)

        if self.class_:
            el.set('class', self.class_)

        if self.style_:
            el.set('style', self.style_)

        el.text = m.group(1)

        return el, m.start(0), m.end(0)

class LlwebExtension(Extension):
    """Markdown extension to handle [u] and [/u] tags."""
    
    def __init__(self, **kwargs):
        self.config = {}
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        InlinesProcessors = [
            ['underline', CustomInlineProcessor(r'\[u\](.*?)\[/u\]',md,'u')],

            ['llweb-color1', CustomInlineProcessor(r'\[c1\](.*?)\[/c1\]',md,'span','color','color:#dc3545;')],
            ['llweb-color2', CustomInlineProcessor(r'\[c2\](.*?)\[/c2\]',md,'span','color','color:#ffc107;')],
            ['llweb-color3', CustomInlineProcessor(r'\[c3\](.*?)\[/c3\]',md,'span','color','color:#28a745;')],
            ['llweb-color4', CustomInlineProcessor(r'\[c4\](.*?)\[/c4\]',md,'span','color','color:#007bff;')],
            ['llweb-color5', CustomInlineProcessor(r'\[c5\](.*?)\[/c5\]',md,'span','color','color:#6c757d;')],
            ['llweb-color6', CustomInlineProcessor(r'\[c6\](.*?)\[/c6\]',md,'span','color','color:#fd7e14;')],

            ['llweb-size1', CustomInlineProcessor(r'\[z1\](.*?)\[/z1\]',md,'span','size','font-size: 3.7rem;')],
            ['llweb-size2', CustomInlineProcessor(r'\[z2\](.*?)\[/z2\]',md,'span','size','font-size: 3.1rem;')],
            ['llweb-size3', CustomInlineProcessor(r'\[z3\](.*?)\[/z3\]',md,'span','size','font-size: 2.6rem;')],
            ['llweb-size4', CustomInlineProcessor(r'\[z4\](.*?)\[/z4\]',md,'span','size','font-size: 2.2rem;')],
            ['llweb-size5', CustomInlineProcessor(r'\[z5\](.*?)\[/z5\]',md,'span','size','font-size: 1.8rem;')],
            ['llweb-size6', CustomInlineProcessor(r'\[z6\](.*?)\[/z6\]',md,'span','size','font-size: 1.5rem;')],
            ['llweb-size7', CustomInlineProcessor(r'\[z7\](.*?)\[/z7\]',md,'span','size','font-size: 1.2rem;')],
            ['llweb-size8', CustomInlineProcessor(r'\[z8\](.*?)\[/z8\]',md,'span','size','font-size: 1.0rem;')],

            ['llweb-align-l', CustomInlineProcessor(r'\[al\](.*?)\[/al\]',md,'p','align-left',  'text-align: left;'  )],
            ['llweb-align-c', CustomInlineProcessor(r'\[ac\](.*?)\[/ac\]',md,'p','align-center','text-align: center;')],
            ['llweb-align-r', CustomInlineProcessor(r'\[ar\](.*?)\[/ar\]',md,'p','align-right', 'text-align: right;' )],
        ]

        for inlines_processors in InlinesProcessors:
            md.inlinePatterns.register(inlines_processors[1], inlines_processors[0], 175)
