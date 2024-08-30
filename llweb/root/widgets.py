from django import forms

class Wysiwyg(forms.Textarea):
    template_name = 'widgets/wysiwyg.html'
