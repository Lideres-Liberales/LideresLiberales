from django.db import models
from django.core.exceptions import ValidationError


class Functionary(models.Model):
    class Meta:
        verbose_name = 'Funcionario Publico'
        verbose_name_plural = 'Funcionarios Publicos'

    name = models.CharField(
        max_length=100
    )

    position = models.CharField(
        max_length=100
    )

    image = models.ImageField(
        verbose_name='Image',
        upload_to='functionaries'
    )

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return f'{self.name} ({self.position})'

    def clean(self):
        if self.parent:
            ancestor = self.parent
            while ancestor:
                if ancestor == self:
                    raise ValidationError('A node cannot be its own descendant.')
                ancestor = ancestor.parent

    def save(self, *args, **kwargs):
        self.clean()

        try:
            official_query = Functionary.objects.filter(id=self.id)

            if official_query.exists():
                if official_query[0].image != self.image:
                    official_query[0].image.delete(save=False)

        except ValueError:
            raise ValueError('Houston, we have a problem')

        super(Functionary, self).save(*args, **kwargs)
