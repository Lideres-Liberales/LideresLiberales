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
        verbose_name='Color (en hexadecimal)',
        max_length=9
    )

    def __str__(self):
        return self.denomination


class Functionary(models.Model, ImageDeletionMixin):
    class Meta:
        abstract = True

    name = models.CharField(
        verbose_name='Nombre',
        max_length=100
    )

    position = models.CharField(
        verbose_name='Cargo',
        max_length=100
    )

    avatar_image = models.ImageField(
        verbose_name='Foto Avatar',
        upload_to='functionaries/avatar'
    )

    perfil_image = models.ImageField(
        verbose_name='Foto Perfil',
        upload_to='functionaries/profile'
    )

    biography = models.TextField(
        verbose_name='Biografia',
        blank=True,
        null=True
    )

    political_party = models.ForeignKey(
        verbose_name='Partido Politico',
        to=PoliticalParty,
        on_delete=models.PROTECT,
        related_name='%(class)s_political_party'
    )

    def save(self, *args, **kwargs):
        self.delete_old_image('image')
        super(Functionary, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ExecutiveBranch(Functionary):
    class Meta:
        verbose_name = 'Miembro poder ejecutivo'
        verbose_name_plural = 'Miembros poder ejecutivo'
        db_table = 'public_executive_branch'

    manager = models.ForeignKey('self',
        verbose_name='Superior',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='team_members'
    )

    height = models.IntegerField(
        verbose_name='Nivel',
        validators=[MinValueValidator(0)],
        default=0
    )

    def save(self, *args, **kwargs):
        self.delete_old_image('image')

        if self.manager:
            self.height = self.manager.height + 1

        super(Functionary, self).save(*args, **kwargs)


class Senator(Functionary):
    class Meta:
        verbose_name = 'Senador'
        verbose_name_plural = 'Senadores'
        db_table = 'public_senator'


class Deputie(Functionary):
    class Meta:
        verbose_name = 'Diputado'
        verbose_name_plural = 'Diputados'
        db_table = 'public_deputie'


class CommunityBoard(Functionary):
    class Meta:
        verbose_name = 'Miembro junta comunal'
        verbose_name_plural = 'Miembros junta comunal'
        db_table = 'public_community_board'


class Councillor(Functionary):
    class Meta:
        verbose_name = 'Consejal'
        verbose_name_plural = 'Consejales'
        db_table = 'public_councillor'
