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

        for field in self.fields.values():
            widget = field.widget.attrs
            classes = 'form-control no-border-input', widget.get('class', '')

            widget['class'] = ' '.join(map(str, classes))
            widget['placeholder'] = field.label

    def persist(self, article_pk):
        instance = super().save(commit=False)
        instance.article_id = article_pk

        return instance.save()
