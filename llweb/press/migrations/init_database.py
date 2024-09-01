from django.db import migrations, models

from users.models import Editor, Provinces
from ..models import *


def clean(text):
    lines = text.splitlines()
    lines_without_tabulation = [line.lstrip() for line in lines]
    text_without_tabulation = '\n'.join(lines_without_tabulation)
    
    return text_without_tabulation


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
    # news fron LLWEB                                                         
    Article.objects.create(
        title='Guillermo Francos se reunió con diputados dialoguistas para trazar la agenda parlamentaria',
        author=walter_hugo,
        featured_image='articles/francos_articulo.jpeg',
        body=clean('''
            El jefe de Gabinete, Guillermo Francos, se reunió en Casa de Gobierno con los bloques dialoguistas de la Cámara de Diputados para informar sobre la implementación de la Ley de Bases, el paquete fiscal y analizar la agenda parlamentaria del próximo semestre, que incluye el proyecto de reforma electoral.
            Estuvieron presentes los presidentes de bloques de la UCR, Rodrigo de Loredo, del PRO, Cristian Ritondo y de Hacemos Coalición Federal, Miguel Ángel Pichetto.
            La reforma electoral fue uno de los ejes centrales del encuentro. El Gobierno pretende eliminar las elecciones PASO y acordar la sanción definitiva de la ley que establece la Boleta Única de Papel a partir del año próximo, que está en consideración del Senado.
        '''),
    )

    Article.objects.create(
        title='El BCRA elimina un 78 el riesgo de emisión',
        author=walter_hugo,
        featured_image='articles/riesgo_de_emisión.jpg',
        body=clean('''
            Desarmó 3,17 billones en estas opciones de liquidez automática que les había vendido a los bancos para que compren bonos al Estado; los analistas destacaron el resultado de la operación
            El Banco Central (BCRA) logró un significativo avance en su intención por cerrar la más imprevisible fuente de emisión monetaria al conseguir que los bancos le rescindan 3,17 billones en opciones de liquidez -los llamados puts- que le habían adquirido por allanarse a financiar al Tesoro Nacional. Es una cifra que representa el 78% del total que buscaba rescatar.
            Para los analistas, se trata de un paso clave para que el Gobierno pueda comenzar a delinear una hoja de ruta progresiva para salir del cepo cambiario, toda vez que fue el propio ministro de Economía, Luis Caputo, quien días atrás en conferencia de prensa identificó ese momento como una bisagra para poder pensar en un crecimiento de la economía, impulsado por el dinamismo que podría tomar la inversión.
        '''),
    )

    Article.objects.create(
        title='evento lideres liberales pba',
        author=walter_hugo,
        featured_image='articles/evento_lideres_liberales_pba.jpeg',
        body=clean('''
            El equipo de Lideres liberales PBA invita a una charla virtual el próximo miércoles 24/7, donde hablaremos sobre nuestra visión y objetivos relacionados a la batalla cultural y el liderazgo en la sociedad actual.
            Durante esta charla exploraremos cómo Ia cultura influye en la toma de decisiones, la importancia de construir nuevos líderes, la comunicación efectiva y las acciones para lograr objetivos. Será una oportunidad para compartir ideas, experiencias y reflexiones.
            Sí querés sumarte a la charla, ingresa a la comunidad desde nuestros enlaces de invitación.
        '''),
    )

    Article.objects.create(
        title='cultura y liderazgoL',
        author=walter_hugo,
        featured_image='articles/cultura_y_liderazgo.png',
        body=clean('''
            Agradecemos a todos los presentes por su participación en la charla sobre cultura y liderazgo a cargo del presidente de Líderes Liberales PBA Moisés Achen que realizamos recientemente. La sesión fue un éxito y dejó una gran impresión en todos nosotros.
            Nuestro orador compartió información valiosa sobre cómo la cultura organizacional impacta en el liderazgo efectivo. Discutimos estrategias para fomentar una cultura de innovación, colaboración y respeto.
            Pero esto es solo el comienzo. Pronto continuaremos con más encuentros sobre cultura y liderazgo. Estén atentos a nuestras próximas invitaciones.
            Gracias nuevamente por su participación y compromiso.
            En unión y libertad.
        '''),
    )

    article = Article(
        title='firma pre acuerdo LL',
        author=walter_hugo,
        featured_image='articles/firma_preacuerdo.jpeg',
        body=clean('''
            Con gran entusiasmo seguimos celebrando la firma del pre acuerdo Nacional, un hito crucial en la construcción para nuestra agrupación. Este acuerdo, posibilta que Líderes Liberales llegue a la Provincia de Mendoza con nuestro referente Marcos Sanchez, también acompañó la firma la Diputada
            Mercedes Llano y Armando Maggistreti Presidente del PD de Mendoza. También tuvieron la oportunidad de firmar el pre acuerdo diversos miembros de CABA y PBA. La unión de líderes y miembros de diferentes regiones demuestra el compromiso compartido por la libertad. Este pre acuerdo es un testimonio de la creciente fuerza de nuestro movimiento, un movimiento que busca construir un legado.
        '''),
    )

    article.save()

    Comment.objects.create(
        name='Laura González',
        email='laura.gonzalez@example.com',
        url='https://www.lideresliberales.org/noticias/pre-acuerdo-mendoza',
        message='¡Excelente noticia! Este pre acuerdo es un gran paso para fortalecer la presencia de Líderes Liberales en todo el país. Felicitaciones a Marcos Sanchez y a todos los involucrados.',
        article=article
    )

    Comment.objects.create(
        name='Juan Pérez',
        email='juan.perez@example.com',
        url='https://www.nacional-liberales.com/noticias/expansion-mendoza',
        message='Me alegra mucho ver que los líderes de diferentes regiones se están uniendo por una causa común. Este acuerdo promete grandes avances para la libertad en Mendoza.',
        article=article
    )

    Comment.objects.create(
        name='Carla Martínez',
        email='carla.martinez@example.com',
        url='https://www.liberalesunidos.org/actualidad/pre-acuerdo-2024',
        message='Un gran logro para el movimiento. La participación de figuras clave como Mercedes Llano y Armando Maggistreti demuestra el impacto y la seriedad del pre acuerdo.',
        article=article
    )

    Comment.objects.create(
        name='Andrés Romero',
        email='andres.romero@example.com',
        url='https://www.proyecto-liberal.net/noticias/firma-pre-acuerdo',
        message='Es inspirador ver cómo Líderes Liberales está expandiendo su influencia en todo el país. Este acuerdo es un testimonio de la creciente fuerza del movimiento.',
        article=article
    )

    Comment.objects.create(
        name='Ana Torres',
        email='ana.torres@example.com',
        url='https://www.movimiento-liberal.com/ultimas-noticias/acuerdo-mendoza',
        message='¡Felicidades por este avance significativo! La unión de líderes de CABA, PBA y Mendoza es un paso crucial para construir un futuro de libertad.',
        article=article
    )

    Comment.objects.create(
        name='Roberto Díaz',
        email='roberto.diaz@example.com',
        url='https://www.agenda-liberales.org/pre-acuerdo-siguiendo-avances',
        message='El compromiso compartido por la libertad es evidente. Este acuerdo no solo refuerza la presencia en Mendoza, sino que también fortalece la unión entre regiones.',
        article=article
    )

    Comment.objects.create(
        name='Marta López',
        email='marta.lopez@example.com',
        url='https://www.liberalesunidos2024.com/noticias/expansion-en-mendoza',
        message='Qué buena noticia para todos los que apoyamos este movimiento. La firma del pre acuerdo es un gran paso hacia la consolidación del proyecto de Líderes Liberales.',
        article=article
    )

    Comment.objects.create(
        name='Javier Morales',
        email='javier.morales@example.com',
        url='https://www.liderazgo-liberal.net/pre-acuerdo-nacional',
        message='Estoy muy contento de ver cómo Líderes Liberales sigue creciendo. Este acuerdo representa un paso importante para llevar nuestras ideas a más provincias.',
        article=article
    )

    Comment.objects.create(
        name='Isabel Fernández',
        email='isabel.fernandez@example.comv',
        url='https://www.nuevo-liberalismo.org/noticias/firma-pre-acuerdo-mendoza',
        message='La firma de este pre acuerdo es una prueba más del compromiso y la seriedad de Líderes Liberales. Espero ver más avances y colaboraciones en el futuro.',
        article=article
    )

    Comment.objects.create(
        name='Federico González',
        email='federico.gonzalez@example.com',
        url='https://www.fuerza-liberal.org/actualidad/acuerdo-nacional-2024',
        message='¡Qué gran noticia! La colaboración entre líderes de diferentes regiones fortalecerá sin duda el movimiento. Felicitaciones a todos los que han hecho posible este acuerdo.',
        article=article
    )


class Migration(migrations.Migration):
    dependencies=[
        ('press', '0001_initial'),
    ]

    operations=[
        migrations.RunPython(set_up),
    ]
