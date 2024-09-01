from django.db import models, transaction

from django.contrib.auth.models import Group
from django.contrib.auth.models import User


class Provinces(models.TextChoices):
    BUENOS_AIRES = 'Buenos Aires', 'Buenos Aires'
    CABA = 'CABA', 'Ciudad Autónoma de Buenos Aires'
    CATAMARCA = 'Catamarca', 'Catamarca'
    CHACO = 'Chaco', 'Chaco'
    CHUBUT = 'Chubut', 'Chubut'
    CORDOBA = 'Córdoba', 'Córdoba'
    CORRIENTES = 'Corrientes', 'Corrientes'
    ENTRE_RIOS = 'Entre Ríos', 'Entre Ríos'
    FORMOSA = 'Formosa', 'Formosa'
    JUJUY = 'Jujuy', 'Jujuy'
    LA_PAMPA = 'La Pampa', 'La Pampa'
    LA_RIOJA = 'La Rioja', 'La Rioja'
    MENDOZA = 'Mendoza', 'Mendoza'
    MISIONES = 'Misiones', 'Misiones'
    NEUQUEN = 'Neuquén', 'Neuquén'
    RIO_NEGRO = 'Río Negro', 'Río Negro'
    SALTA = 'Salta', 'Salta'
    SAN_JUAN = 'San Juan', 'San Juan'
    SAN_LUIS = 'San Luis', 'San Luis'
    SANTA_CRUZ = 'Santa Cruz', 'Santa Cruz'
    SANTA_FE = 'Santa Fe', 'Santa Fe'
    SANTIAGO_DEL_ESTERO = 'Santiago del Estero', 'Santiago del Estero'
    TIERRA_DEL_FUEGO = 'Tierra del Fuego', 'Tierra del Fuego'
    TUCUMAN = 'Tucumán', 'Tucumán'


## ------------- Seccion Profile -------------- ##
class Profile(models.Model):
    image = models.ImageField(
        verbose_name='Imagen',
        upload_to='profiles',
        null=True,
        blank=True
    )

    user = models.OneToOneField(
        related_name='profile',
        to=User,
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        try:
            profile_query = Profile.objects.filter(id=self.id)

            if profile_query.exists():
                if profile_query[0].image != self.image:
                    profile_query[0].image.delete(save=False)

        except ValueError:
            raise ValueError('Houston, tenemos un problema')

        super(Profile, self).save(*args, **kwargs)


## ------------- Seccion AbstractUser ------------ ##
class AbstractUser(User):
    class Meta:
        abstract = True

    dni = models.CharField(
        verbose_name='DNI',
        max_length=50
    )

    movil_phone = models.CharField(
        verbose_name='Telefono movil',
        max_length=17
    )

    province = models.CharField(
        verbose_name='Provincia',
        choices=Provinces.choices,
        default=Provinces.BUENOS_AIRES,
        max_length=100
    )

    creation = models.DateTimeField(auto_now_add=True)
    modification = models.DateTimeField(auto_now=True)

    def groups_name(self):
        return ''

    # TODO: from django.db import models, transaction
    def save(self, *args, **kwargs):
        with transaction.atomic():
            super(AbstractUser, self).save(*args, **kwargs)

            if not self.groups.all():
                self.groups.add(Group.objects.get(name=self.groups_name()))

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class BoardOfDirectors(AbstractUser):
    class Meta:
        verbose_name = 'Miembro - Mesa directiva'
        verbose_name_plural = 'Mesa Directiva'

    def groups_name(self):
        return 'BoardOfDirectorsGroups'


class Member(AbstractUser):
    class Meta:
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'

    def groups_name(self):
        return 'MemberGroups'


class Editor(AbstractUser):
    class Meta:
        verbose_name = 'Editor'
        verbose_name_plural = 'Editores'

    def groups_name(self):
        return 'EditorGroups'