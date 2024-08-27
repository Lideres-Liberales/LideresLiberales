from django import forms

class Wysiwyg(forms.Textarea):
    template_name = 'widgets/wysiwyg.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        if context["widget"]["value"] is None:
            context["widget"]["value"] = ''

        return context
