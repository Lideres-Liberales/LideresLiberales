from django.db import models

from django.core.files.storage import default_storage
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class ImageDeletionMixin:
    def delete_old_image(self, image_field_name):
        try:
            if self.pk:
                old_instance = self.__class__.objects.get(pk=self.pk)
                old_image = getattr(old_instance, image_field_name, None)
                new_image = getattr(self, image_field_name, None)

                if old_image != new_image:
                    if old_image and default_storage.exists(old_image.name):
                        default_storage.delete(old_image.name)

        except ValueError:
            raise ValueError('Houston, we have a problem')


class PoliticalParty(models.Model):
    class Meta:
        verbose_name = 'Partido Politico'
        verbose_name_plural = 'Partidos Politicos'
        db_table = 'public_political_parties'

    denomination = models.CharField(
        verbose_name='Denominacion',
        max_length=100
    )

    color = models.CharField(
        verbose_name='Color',
        max_length=9
    )


class Functionary(models.Model, ImageDeletionMixin):
    class Meta:
        verbose_name = 'Funcionario Publico'
        verbose_name_plural = 'Funcionarios Publicos'
        db_table = 'public_functionaries'

    name = models.CharField(
        verbose_name='Nombre',
        max_length=100
    )

    position = models.CharField(
        verbose_name='Cargo',
        max_length=100
    )

    image = models.ImageField(
        verbose_name='Avatar',
        upload_to='functionaries/avatar'
    )

    height = models.IntegerField(
        verbose_name='Nivel',
        validators=[MinValueValidator(0)],
        default=0
    )

    manager = models.ForeignKey('self',
        verbose_name='Superior',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='team_members'
    )

    political_party = models.ForeignKey(
        verbose_name='Partido Politico',
        on_delete=models.PROTECT,
        to=PoliticalParty,
        related_name='political_party',
    )

    def save(self, *args, **kwargs):
        self.delete_old_image('image')

        if self.manager:
            self.height = self.manager.height + 1

        super(Functionary, self).save(*args, **kwargs)


class FunctionaryPerfil(models.Model, ImageDeletionMixin):
    class Meta:
        verbose_name = 'Funcionario Publico - Perfil'
        verbose_name_plural = 'Funcionarios Publicos - Perfiles'
        db_table = 'public_functionary_profiles'

    biography = models.CharField(
        verbose_name='Biografia',
        max_length=4096
    )

    image = models.ImageField(
        verbose_name='Foto Perfil',
        upload_to='functionaries/profile'
    )

    functionary = models.OneToOneField(
        related_name='profile',
        to=Functionary,
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        self.delete_old_image('image')
        super(FunctionaryPerfil, self).save(*args, **kwargs)
