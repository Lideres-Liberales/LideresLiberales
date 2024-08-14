from datetime import time, date, timedelta

from django.db import migrations, models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from ..models import *


def set_up(apps, scheme_editor):
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % Functionaries                                                         %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    functionaries = []

    functionaries.append(
        Functionary.objects.create(
            name = 'Javier Milei',
            position = 'Presidente de la Nacion',
            image = 'functionaries/avatar_milei.png',
            height = 0
        )
    )

    functionaries.append(
        Functionary.objects.create(
            name = 'Victoria Villaruel',
            position = 'Vicepresidencia de la Nación',
            image = 'functionaries/avatar_villaruel.png',
            height = 0
        )
    )

    functionaries.append(
        Functionary.objects.create(
            name = 'Karina Milei',
            position = 'Secretaria gral de presidencia',
            image = 'functionaries/avatar_karina.png',
            height = 1,
            manager = functionaries[0]
        )
    )

    functionaries.append(
        Functionary.objects.create(
            name = 'Guillermo Francos',
            position = 'Jefe de Gabinete',
            image = 'functionaries/avatar_francos.png',
            height = 1,
            manager = functionaries[0]
        )
    )

    functionaries.append(
        Functionary.objects.create(
            name = 'Manuel Adorni',
            position = 'Vocero',
            image = 'functionaries/avatar_adorni.png',
            height = 1,
            manager = functionaries[0]
        )
    )

    functionaries.append(
        Functionary.objects.create(
            name = 'Sandra Pettovello',
            position = 'Ministerio de Capital Humano',
            image = 'functionaries/avatar_pettovello.png',
            height = 2,
            manager = functionaries[3]
        )
    )

    functionaries.append(
        Functionary.objects.create(
            name = 'Luis Petri',
            position = 'Ministerio de Defensa',
            image = 'functionaries/avatar_petri.png',
            height = 2,
            manager = functionaries[3]
        )
    )

    functionaries.append(
        Functionary.objects.create(
            name = 'Federico Sturzenegger',
            position = 'Ministro de Desregulación y Transformación del Estado',
            image = 'functionaries/avatar_sturzenegger.png',
            height = 2,
            manager = functionaries[3]
        )
    )

    functionaries.append(
        Functionary.objects.create(
            name = 'Luis Caputo',
            position = 'Ministerio de Economía',
            image = 'functionaries/avatar_caputo.png',
            height = 2,
            manager = functionaries[3]
        )
    )

    functionaries.append(
        Functionary.objects.create(
            name = 'Mariano Cúneo Libarona',
            position = 'Ministerio de Justicia',
            image = 'functionaries/avatar_cuneo_libarona.png',
            height = 2,
            manager = functionaries[3]
        )
    )

    functionaries.append(
        Functionary.objects.create(
            name = 'Diana Mondino',
            position = 'Ministerio de Relaciones Exteriores, Comercio Internacional y Culto',
            image = 'functionaries/avatar_mondino.png',
            height = 2,
            manager = functionaries[3]
        )
    )

    functionaries.append(
        Functionary.objects.create(
            name = 'Mario Russo',
            position = 'Ministerio de Salud',
            image = 'functionaries/avatar_russo.png',
            height = 2,
            manager = functionaries[3]
        )
    )

    functionaries.append(
        Functionary.objects.create(
            name = 'Patricia Bullrich',
            position = 'Ministerio de Seguridad',
            image = 'functionaries/avatar_bulrich.png',
            height = 2,
            manager = functionaries[3]
        )
    )

    for functionary in functionaries:
        functionary.save()

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % Root                                                                  %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    root = User(
        username='root',
        first_name='root',
        last_name='root',
        email='root@root.com',
        is_superuser=True,
        is_staff=True,
        is_active=True,
    )

    root.set_password('root')
    root.save()


class Migration(migrations.Migration):
    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(set_up),
    ]
