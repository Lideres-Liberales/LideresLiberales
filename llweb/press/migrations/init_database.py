from django.db import migrations, models

from users.models import Editor, Provinces
from ..models import *


def set_up(apps, scheme_editor):
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % Author                                                                %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    walter_hugo = Editor(
        username='walter_hugo',
        first_name='Walter',
        last_name='Hugo',
        email='walter_hugo@email.com',
        dni='93986590',
        province=Provinces.CABA,
        movil_phone='02954 6789 2345',
        is_superuser=False,
        is_staff=True,
        is_active=True
    )

    walter_hugo.set_password('1234')
    walter_hugo.save()

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % Articles                                                              %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Article.objects.create(
        title='Guillermo Francos se reunió con diputados dialoguistas para trazar la agenda parlamentaria',
        author=walter_hugo,
        featured_image='articles/francos_articulo.jpeg',
        body='''
            El jefe de Gabinete, Guillermo Francos, se reunió en Casa de Gobierno con los bloques dialoguistas de la Cámara de Diputados para informar sobre la implementación de la Ley de Bases, el paquete fiscal y analizar la agenda parlamentaria del próximo semestre, que incluye el proyecto de reforma electoral.
            Estuvieron presentes los presidentes de bloques de la UCR, Rodrigo de Loredo, del PRO, Cristian Ritondo y de Hacemos Coalición Federal, Miguel Ángel Pichetto.
            La reforma electoral fue uno de los ejes centrales del encuentro. El Gobierno pretende eliminar las elecciones PASO y acordar la sanción definitiva de la ley que establece la Boleta Única de Papel a partir del año próximo, que está en consideración del Senado.
        ''',
    )

    Article.objects.create(
        title='El BCRA elimina un 78 el riesgo de emisión',
        author=walter_hugo,
        featured_image='articles/riesgo_de_emisión.jpg',
        body='''
            Desarmó 3,17 billones en estas opciones de liquidez automática que les había vendido a los bancos para que compren bonos al Estado; los analistas destacaron el resultado de la operación
            El Banco Central (BCRA) logró un significativo avance en su intención por cerrar la más imprevisible fuente de emisión monetaria al conseguir que los bancos le rescindan 3,17 billones en opciones de liquidez -los llamados puts- que le habían adquirido por allanarse a financiar al Tesoro Nacional. Es una cifra que representa el 78% del total que buscaba rescatar.
            Para los analistas, se trata de un paso clave para que el Gobierno pueda comenzar a delinear una hoja de ruta progresiva para salir del cepo cambiario, toda vez que fue el propio ministro de Economía, Luis Caputo, quien días atrás en conferencia de prensa identificó ese momento como una bisagra para poder pensar en un crecimiento de la economía, impulsado por el dinamismo que podría tomar la inversión.
        ''',
    )

    Article.objects.create(
        title='evento lideres liberales pba',
        author=walter_hugo,
        featured_image='articles/evento_lideres_liberales_pba.jpeg',
        body='''
            El equipo de Lideres liberales PBA invita a una charla virtual el próximo miércoles 24/7, donde hablaremos sobre nuestra visión y objetivos relacionados a la batalla cultural y el liderazgo en la sociedad actual.
            Durante esta charla exploraremos cómo Ia cultura influye en la toma de decisiones, la importancia de construir nuevos líderes, la comunicación efectiva y las acciones para lograr objetivos. Será una oportunidad para compartir ideas, experiencias y reflexiones.
            Sí querés sumarte a la charla, ingresa a la comunidad desde nuestros enlaces de invitación.
        ''',
    )

    Article.objects.create(
        title='cultura y liderazgoL',
        author=walter_hugo,
        featured_image='articles/cultura_y_liderazgo.png',
        body='''
            Agradecemos a todos los presentes por su participación en la charla sobre cultura y liderazgo a cargo del presidente de Líderes Liberales PBA Moisés Achen que realizamos recientemente. La sesión fue un éxito y dejó una gran impresión en todos nosotros.
            Nuestro orador compartió información valiosa sobre cómo la cultura organizacional impacta en el liderazgo efectivo. Discutimos estrategias para fomentar una cultura de innovación, colaboración y respeto.
            Pero esto es solo el comienzo. Pronto continuaremos con más encuentros sobre cultura y liderazgo. Estén atentos a nuestras próximas invitaciones.
            Gracias nuevamente por su participación y compromiso.
            En unión y libertad.
        ''',
    )

    Article.objects.create(
        title='firma pre acuerdo LL',
        author=walter_hugo,
        featured_image='articles/firma_preacuerdo.jpeg',
        body='''
            Con gran entusiasmo seguimos celebrando la firma del pre acuerdo Nacional, un hito crucial en la construcción para nuestra agrupación. Este acuerdo, posibilta que Líderes Liberales llegue a la Provincia de Mendoza con nuestro referente Marcos Sanchez, también acompañó la firma la Diputada
            Mercedes Llano y Armando Maggistreti Presidente del PD de Mendoza. También tuvieron la oportunidad de firmar el pre acuerdo diversos miembros de CABA y PBA. La unión de líderes y miembros de diferentes regiones demuestra el compromiso compartido por la libertad. Este pre acuerdo es un testimonio de la creciente fuerza de nuestro movimiento, un movimiento que busca construir un legado.
        ''',
    )


class Migration(migrations.Migration):
    dependencies = [
        ('press', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(set_up),
    ]
