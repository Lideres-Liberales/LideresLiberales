from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm


class Home(TemplateView):
    template_name = 'home.html'


class Cabinet(TemplateView):
    template_name = 'cabinet.html'


class Join(FormView):
    template_name = 'join.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    # def form_valid(self, form):
    #     # Aquí puedes manejar el formulario, enviar un correo, etc.
    #     # form.cleaned_data contiene los datos validados del formulario
    #     print(form.cleaned_data)  # Solo un ejemplo de cómo acceder a los datos
    #     return super().form_valid(form)
    def form_valid(self, form):
        try:
            form.send_mail()
            messages.success(self.request, 'Su mensaje se ha enviado correctamente.')
        except:
            messages.error(self.request, 'Error interno, disculpe las molestias.')

        return super().form_valid(form)

class Events(TemplateView):
    template_name = 'events.html'
