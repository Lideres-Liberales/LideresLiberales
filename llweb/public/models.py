from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


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


class Functionary(models.Model):
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

    def clean_manager(self):
        if self.manager:
            ancestor = self.manager
            while ancestor:
                if ancestor == self:
                    raise ValidationError('A node cannot be its own descendant.')
                ancestor = ancestor.manager

    def save(self, *args, **kwargs):
        self.clean()

        try:
            if self.manager:
                self.height = self.manager.height + 1

            functionary_query = Functionary.objects.filter(id=self.id)

            if functionary_query.exists():
                if functionary_query[0].image != self.image:
                    functionary_query[0].image.delete(save=False)

        except ValueError:
            raise ValueError('Houston, we have a problem')

        super(Functionary, self).save(*args, **kwargs)


class FunctionaryPerfil(models.Model):
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
        on_delete=models.PROTECT
    )
