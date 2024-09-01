from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic.edit import FormView

from .forms import ContactForm


class Join(FormView):
    template_name = 'join.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        try:
            form.send_mail()
            messages.success(self.request, 'Su mensaje se ha enviado correctamente.')
        except:
            messages.error(self.request, 'Error interno, disculpe las molestias.')

        return super().form_valid(form)
