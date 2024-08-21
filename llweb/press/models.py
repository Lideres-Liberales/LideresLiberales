from django.db import models
from django.core.validators import EmailValidator

from users.models import Editor


class Article(models.Model):
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    title = models.CharField(
        verbose_name='Titulo',
        max_length=50
    )

    author = models.ForeignKey(
        related_name='article',
        to=Editor,
        on_delete=models.CASCADE
    )

    featured_image = models.ImageField(
        verbose_name='Imagen Destacada',
        upload_to='articles',
        blank=True,
        null=True
    )

    body = models.TextField(
        verbose_name='Cuerpo'
    )

    creation = models.DateTimeField(auto_now_add=True)
    modification = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    name = models.CharField(
        verbose_name='Nombre',
        max_length=50
    )

    email = models.EmailField(
        verbose_name='Correo electronico',
        unique=False,
        validators=[EmailValidator()]
    )

    url = models.URLField(
        verbose_name='Url',
        max_length=200
    )

    message = models.CharField(
        verbose_name='Nombre',
        max_length=200
    )

    article = models.ForeignKey(
        related_name='comments',
        to=Article,
        on_delete=models.CASCADE
    )

    creation = models.DateTimeField(auto_now_add=True)
    modification = models.DateTimeField(auto_now=True)
