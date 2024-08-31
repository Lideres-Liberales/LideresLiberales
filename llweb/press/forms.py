from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'name', 'email', 'url']
        widgets = {
            'message': forms.Textarea(
                attrs={
                    'class': 'fixed-size-textarea',
                    'rows': 5,
                    'cols': 40
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        base_classes = 'form-control no-border-input'

        for field_name, field in self.fields.items():
            widget = field.widget.attrs
            widget['placeholder'] = field.label

            extra_class = widget.get('class', '') + ' '

            if self.is_bound and field_name in self.errors:
                widget['class'] = extra_class+ base_classes + ' is-invalid'
            else:
                widget['class'] = extra_class+ base_classes

    def persist(self, article_pk):
        instance = super().save(commit=False)
        instance.article_id = article_pk

        return instance.save()
