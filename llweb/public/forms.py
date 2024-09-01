from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput( attrs={
            'placeholder': 'Escriba su nombre'
        })
    )

    movil_phone = forms.CharField(
        widget=forms.TextInput( attrs={
            'placeholder': 'Escriba su celular',
            'pattern': r'\+?\d[\d\s\-\(\)]*'
        })
    )

    email = forms.EmailField(
        widget = forms.EmailInput( attrs = {
            'placeholder': 'Escriba su email',
            'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
        })
    )


    address = forms.CharField(
        max_length=100,
        widget=forms.TextInput( attrs={
            'placeholder': 'Escriba su dirección',
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if self.is_bound and field_name in self.errors:
                field.widget.attrs['class'] = 'form-control is-invalid'
            else:
                field.widget.attrs['class'] = 'form-control'

    def send_mail(self):
        data = self.cleaned_data
        send_mail(

            'Informacion de contacto',
            f"Nombre: {data.get('name')}\n" + 
            f"Celular: {data.get('movil_phone')}\n" + 
            f"Email: {data.get('email')}\n" + 
            f"Direccion: {data.get('address')}",

            data.get('correo_electronico'),
            ["wololo@secretaria.com"],
            fail_silently=False
        )
