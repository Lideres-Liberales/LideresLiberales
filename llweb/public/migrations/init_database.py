from django.db import transaction

from django.db import migrations, models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from ..models import *


def clear_text(input_string):
    lines = input_string.split('\n')
    stripped_lines = [line.lstrip() for line in lines]
    return ''.join(stripped_lines)


def set_up(apps, scheme_editor):
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % Political Party                                                       %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    parties = []

    parties.append( # 0
        PoliticalParty.objects.create(
            denomination = 'Independiente - sin afiliacion',
            color = '#7f7f7f'
        )
    )

    parties.append( # 1
        PoliticalParty.objects.create(
            denomination = 'La Libertad Avanza',
            color = '#6c4c99'
        )
    )

    parties.append( # 2
        PoliticalParty.objects.create(
            denomination = 'Propuesta Republicana',
            color = '#ffd700'
        )
    )

    parties.append( # 3
        PoliticalParty.objects.create(
            denomination = 'Unión Cívica Radical',
            color = '#e10019'
        )
    )

    parties.append(
        PoliticalParty.objects.create(
            denomination = 'Partido Justicialista',
            color = '#318ce7'
        )
    )

    parties.append(
        PoliticalParty.objects.create(
            denomination = 'Unión por la Patria',
            color = '#009fe3'
        )
    )

    for party in parties:
        party.save()

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % Functionaries                                                         %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    functionaries = []

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $ Executive Branch                                                      $
    functionaries.append(
        ExecutiveBranch.objects.create(
            name = 'Javier Milei',
            position = 'Presidente de la Nacion',
            avatar_image = 'functionaries/avatar/milei.png',
            perfil_image = 'functionaries/profile/milei.jpeg',
            height = 0,
            political_party = parties[1],
            biography = clear_text("""
                Nació el 22 de Octubre de 1970 en CABA. Economista, político y 
                docente Argentino. Liberal Libertario Anarco-Capitalista. 
                Graduado en Economía en la Universidad de Belgrano. Obtuvo un 
                doctorado en Economía en la Universidad de Buckingham en el 
                Reino Unido. Ha trabajado como profesor universitario y en 
                Instituciones Financieras y de Investigación Económica. Milei 
                se dio a conocer en la escena pública Argentina a partir del 
                2016 participando en debates en programas de televisión y de 
                radio, expresando opiniones radicales en temas económicos y 
                sociales. Se identifica como un defensor del liberalismo 
                clásico y critica el intervencionismo estatal en la economía, 
                abogando por la reducción del tamaño del gobierno y la 
                promoción de políticas liberales en materia fiscal y monetaria.
                En 2021, Milei anunció su candidatura a diputado nacional 
                por la Ciudad Autónoma de Buenos Aires y posteriormente, él 
                mismo fundó el partido "La Libertad Avanza" destacándose 
                durante su campaña electoral por su retórica apasionada y sus 
                críticas a la clase política tradicional. Logró un notable 
                apoyo popular, especialmente entre los sectores más jóvenes 
                y desencantados con el sistema político argentino.
            """)
        )
    )

    functionaries.append(
        ExecutiveBranch.objects.create(
            name = 'Victoria Villaruel',
            position = 'Vicepresidencia de la Nación',
            avatar_image = 'functionaries/avatar/villaruel.png',
            perfil_image = 'functionaries/profile/villaruel.jpeg',
            height = 0,
            political_party = parties[1],
            biography = clear_text("""
                Nació el 13 de abril de 1975 en Buenos Aires. Abogada, 
                activista y política argentina. Ha dedicado gran parte de su 
                carrera a defender los derechos de las víctimas de las 
                organizaciones guerrilleras de los años 70. Es fundadora del 
                Centro de Estudios Legales sobre el Terrorismo y sus Víctimas 
                (CELTYV). Actualmente desempeña el cargo de Vicepresidente de 
                Argentina desde diciembre del 2023 destacándose por su firme 
                ideología. Su vida y obra reflejan un profundo compromiso con 
                los valores que defiende.
            """)
        )
    )

    functionaries.append(
        ExecutiveBranch.objects.create(
            name = 'Karina Milei',
            position = 'Secretaria gral de presidencia',
            avatar_image = 'functionaries/avatar/karina.png',
            perfil_image = 'functionaries/profile/karina.jpeg',
            height = 1,
            manager = functionaries[0],
            political_party = parties[1],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    functionaries.append(
        ExecutiveBranch.objects.create(
            name = 'Guillermo Francos',
            position = 'Jefe de Gabinete',
            avatar_image = 'functionaries/avatar/francos.png',
            perfil_image = 'functionaries/profile/francos.jpeg',
            height = 1,
            manager = functionaries[0],
            political_party = parties[1],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    functionaries.append(
        ExecutiveBranch.objects.create(
            name = 'Manuel Adorni',
            position = 'Vocero',
            avatar_image = 'functionaries/avatar/adorni.png',
            perfil_image = 'functionaries/profile/adorni.jpeg',
            height = 1,
            manager = functionaries[0],
            political_party = parties[1],
            biography = clear_text("""
                Nació el 28 de Febrero de 1980 en La Plata. Analista 
                económico, consultor empresarial y docente seleccionado por 
                Javier Milei para desempeñarse como vocero presidencial, la 
                voz del presidente. Su principal responsabilidad se basa en 
                comunicar y representar al gobierno en una variedad de asuntos 
                y eventos oficiales, demostrando su capacidad para transmitir 
                de manera efectiva los mensajes y las políticas del gobierno.
            """)
        )
    )

    functionaries.append(
        ExecutiveBranch.objects.create(
            name = 'Sandra Pettovello',
            position = 'Ministerio de Capital Humano',
            avatar_image = 'functionaries/avatar/pettovello.png',
            perfil_image = 'functionaries/profile/pettovello.jpeg',
            height = 2,
            manager = functionaries[3],
            political_party = parties[1],
            biography = clear_text("""
                Periodista y política argentina nacida el 6 de abril de 1968 
                en Buenos Aires. Actualmente, ocupa el cargo de ministra de 
                Capital Humano en la administración de Javier Milei desde el 
                10 de diciembre de 2023. Pettovello se presenta como 
                especialista en temas familiares y sociales, con una 
                licenciatura en Ciencias para la Familia de la Universidad 
                Austral. Además de su trayectoria periodística, ha asumido un 
                papel relevante en la política argentina, siendo electa 
                diputada nacional por la Ciudad Autónoma de Buenos Aires antes 
                de aceptar la propuesta de Milei para liderar el nuevo 
                ministerio que fusiona áreas como Educación, Trabajo, 
                Desarrollo Social y Salud.
            """)
        )
    )

    functionaries.append(
        ExecutiveBranch.objects.create(
            name = 'Luis Petri',
            position = 'Ministerio de Defensa',
            avatar_image = 'functionaries/avatar/petri.png',
            perfil_image = 'functionaries/profile/petri.jpeg',
            height = 2,
            manager = functionaries[3],
            political_party = parties[3],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    functionaries.append(
        ExecutiveBranch.objects.create(
            name = 'Federico Sturzenegger',
            position = 'Ministro de Desregulación',
            avatar_image = 'functionaries/avatar/sturzenegger.png',
            perfil_image = 'functionaries/profile/sturzenegger.jpeg',
            height = 2,
            manager = functionaries[3],
            political_party = parties[1],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    functionaries.append(
        ExecutiveBranch.objects.create(
            name = 'Luis Caputo',
            position = 'Ministerio de Economía',
            avatar_image = 'functionaries/avatar/caputo.png',
            perfil_image = 'functionaries/profile/caputo.jpeg',
            height = 2,
            manager = functionaries[3],
            political_party = parties[2],
            biography = clear_text("""
                Conocido como “Toto”, es un economista argentino nacido el 21 
                de abril de 1965 en Buenos Aires. Actualmente, ocupa el cargo 
                de Ministro de Economía de la Nación Argentina en la 
                administración de Javier Milei desde el 10 de diciembre de 
                2023. A lo largo de su carrera, Caputo ha desempeñado roles 
                destacados en instituciones financieras y gubernamentales, es 
                una figura influyente en la economía argentina, con una 
                trayectoria sólida.
            """)
        )
    )

    functionaries.append(
        ExecutiveBranch.objects.create(
            name = 'Mariano Cúneo Libarona',
            position = 'Ministerio de Justicia',
            avatar_image = 'functionaries/avatar/cuneo_libarona.png',
            perfil_image = 'functionaries/profile/cuneo_libarona.jpeg',
            height = 2,
            manager = functionaries[3],
            political_party = parties[1],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    functionaries.append(
        ExecutiveBranch.objects.create(
            name = 'Diana Mondino',
            position = 'Ministerio de Relaciones Exteriores',
            avatar_image = 'functionaries/avatar/mondino.png',
            perfil_image = 'functionaries/profile/mondino.jpeg',
            height = 2,
            manager = functionaries[3],
            political_party = parties[1],
            biography = clear_text("""
                Nació el 8 de Agosto de 1958 en Córdoba Septiembre de 1977 en 
                Corrientes. Estudió economía en la Universidad de Córdoba e 
                hizo un Master en Marketing y Economía en España. En 2008 
                llevó la antorcha olímpica en los Juegos Olímpicos que se 
                realizaron en Beijing, China. En 2023 fue Diputada de la 
                Cámara de Diputados representando a la Ciudad de Buenos Aires; 
                actualmente es Ministra de Relaciones Exteriores, Comercio 
                Internacional y Culto que asumió el 10 de diciembre del 2023. 
                Diana sabe hablar perfectamente en Inglés, Portugués y sabe un 
                poco de Francés.
            """)
        )
    )

    functionaries.append(
        ExecutiveBranch.objects.create(
            name = 'Mario Russo',
            position = 'Ministerio de Salud',
            avatar_image = 'functionaries/avatar/russo.png',
            perfil_image = 'functionaries/profile/russo.jpeg',
            height = 2,
            manager = functionaries[3],
            political_party = parties[1],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    functionaries.append(
        ExecutiveBranch.objects.create(
            name = 'Patricia Bullrich',
            position = 'Ministerio de Seguridad',
            avatar_image = 'functionaries/avatar/bulrich.png',
            perfil_image = 'functionaries/profile/bullrich.jpeg',
            height = 2,
            manager = functionaries[3],
            political_party = parties[2],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $ Deputies                                                              $
    functionaries.append(
        Deputie.objects.create(
            name = 'Martín Menem',
            position = 'Diputado',
            is_president = True,
            avatar_image = 'functionaries/avatar/martin_menem.png',
            perfil_image = 'functionaries/profile/martin_menem.png',
            political_party = parties[1],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    functionaries.append(
        Deputie.objects.create(
            name = 'Alberto Gustavo Arancibia Rodríguez',
            position = 'Diputado',
            avatar_image = 'functionaries/avatar/alberto_arancibia_rodríguez.png',
            perfil_image = 'functionaries/profile/alberto_arancibia_rodríguez.png',
            political_party = parties[1],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    functionaries.append(
        Deputie.objects.create(
            name = 'Gabriel Bornoroni',
            position = 'Diputado',
            avatar_image = 'functionaries/avatar/gabriel_bornoroni.png',
            perfil_image = 'functionaries/profile/gabriel_bornoroni.png',
            political_party = parties[1],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    functionaries.append(
        Deputie.objects.create(
            name = 'Lisandro Almirón',
            position = 'Diputado',
            avatar_image = 'functionaries/avatar/lisandro_almiron.png',
            perfil_image = 'functionaries/profile/lisandro_almiron.png',
            political_party = parties[1],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    functionaries.append(
        Deputie.objects.create(
            name = 'Pablo Ansaloni',
            position = 'Diputado',
            avatar_image = 'functionaries/avatar/pablo_ansaloni.png',
            perfil_image = 'functionaries/profile/pablo_ansaloni.png',
            political_party = parties[1],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $ Senators                                                              $
    functionaries.append(
        Senator.objects.create(
            name = 'Bartolomé Esteban Abdala',
            position = 'Senador',
            avatar_image = 'functionaries/avatar/bartolome_esteban_abdala.png',
            perfil_image = 'functionaries/profile/bartolome_esteban_abdala.jpeg',
            political_party = parties[1],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    functionaries.append(
        Senator.objects.create(
            name = 'Bruno Olivera Lucero',
            position = 'Senador',
            avatar_image = 'functionaries/avatar/bruno_antonio_olivera_lucero.png',
            perfil_image = 'functionaries/profile/bruno_antonio_olivera_lucero.jpg',
            political_party = parties[1],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    functionaries.append(
        Senator.objects.create(
            name = 'Ezequiel Atauche',
            position = 'Senador',
            avatar_image = 'functionaries/avatar/ezequiel_atauche.png',
            perfil_image = 'functionaries/profile/ezequiel_atauche.jpeg',
            political_party = parties[1],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    functionaries.append(
        Senator.objects.create(
            name = 'Francisco Paoltroni',
            position = 'Senador',
            avatar_image = 'functionaries/avatar/francisco_manuel_paoltroni.png',
            perfil_image = 'functionaries/profile/francisco_manuel_paoltroni.jpeg',
            political_party = parties[1],
            biography = clear_text("""
                En construccion
            """)
        )
    )

    functionaries.append(
        Senator.objects.create(
            name = 'Ivanna Marcela Arrascaeta',
            position = 'Senador',
            avatar_image = 'functionaries/avatar/ivanna_marcela_arrascaeta.png',
            perfil_image = 'functionaries/profile/ivanna_marcela_arrascaeta.jpg',
            political_party = parties[1],
            biography = clear_text("""
                En construccion
            """)
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
