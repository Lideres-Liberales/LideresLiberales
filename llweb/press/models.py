from django.db import models, transaction
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

    prev_article = models.OneToOneField('self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='related_next_article'
    )

    next_article = models.OneToOneField('self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='related_prev_article'
    )

    creation = models.DateTimeField(auto_now_add=True)
    modification = models.DateTimeField(auto_now=True)

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            first_article = Article.objects.filter(prev_article__isnull=True).exclude(id=self.id).first()

            if first_article and first_article != self:
                first_article.prev_article = self
                first_article.save(update_fields=['prev_article'])

                self.prev_article = None
                self.next_article = first_article
                self.save(update_fields=['prev_article', 'next_article'])

        else:
            super().save(*args, **kwargs)


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
