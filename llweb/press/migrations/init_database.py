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
    # Fake news                                                               #
    Article.objects.create(
        title='La Revolución de la Inteligencia Artificial en 2024',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            En 2024, la inteligencia artificial ha avanzado a pasos agigantados, permitiendo desarrollos sin precedentes en automatización y análisis de datos.
        ''',
    )

    Article.objects.create(
        title='Nuevas Tecnologías en el Desarrollo de Aplicaciones Móviles',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            Las nuevas herramientas de desarrollo permiten ahora una integración más sencilla de funciones avanzadas en aplicaciones móviles, mejorando la experiencia del usuario.
        ''',
    )

    Article.objects.create(
        title='Cómo la Computación Cuántica Transformará el Desarrollo de Software',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            La llegada de la computación cuántica promete revolucionar el campo del desarrollo de software, permitiendo resolver problemas complejos a una velocidad sin precedentes.
        ''',
    )

    Article.objects.create(
        title='El Impacto del 5G en la Programación de Dispositivos IoT',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            La implementación de redes 5G está facilitando la creación de dispositivos IoT más rápidos y eficientes, con una conectividad mejorada y menor latencia.
        ''',
    )

    Article.objects.create(
        title='Blockchain: Más Allá de las Criptomonedas',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            La tecnología blockchain está encontrando nuevas aplicaciones en la gestión de datos y la seguridad, más allá de su uso en criptomonedas.
        ''',
    )

    Article.objects.create(
        title='El Futuro de la Realidad Aumentada en el Desarrollo Web',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            La realidad aumentada está comenzando a integrarse en el desarrollo web, ofreciendo nuevas formas de interacción y visualización para los usuarios.
        ''',
    )

    Article.objects.create(
        title='Desarrollo Sostenible: El Rol de la Energía Verde en la Industria del Software',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            La industria del software está adoptando prácticas sostenibles, incluyendo el uso de energías renovables para reducir su huella de carbono.
        ''',
    )

    Article.objects.create(
        title='El Renacer del Desarrollo de Juegos en 2024',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            Con avances en gráficos y procesamiento, el desarrollo de juegos ha alcanzado un nuevo nivel de realismo y complejidad en 2024.
        ''',
    )

    Article.objects.create(
        title='Cómo la Automatización está Redefiniendo el Desarrollo de Software',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            La automatización está cambiando la forma en que se desarrolla el software, desde la codificación hasta las pruebas y el mantenimiento.
        ''',
    )

    Article.objects.create(
        title='Tendencias Emergentes en el Desarrollo de APIs',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            Las nuevas tendencias en el desarrollo de APIs están facilitando una mayor interoperabilidad y flexibilidad en la integración de sistemas.
        ''',
    )

    Article.objects.create(
        title='La Evolución de los Lenguajes de Programación en la Última Década',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            En la última década, hemos visto una evolución significativa en los lenguajes de programación, con nuevas opciones que mejoran la productividad y la eficiencia.
        ''',
    )

    Article.objects.create(
        title='Seguridad en la Nube: Nuevas Estrategias para Proteger tus Datos',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            A medida que más datos se almacenan en la nube, las estrategias de seguridad están evolucionando para proteger mejor la información crítica.
        ''',
    )

    Article.objects.create(
        title='El Auge de los Microservicios en el Desarrollo de Software',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            Los microservicios se están convirtiendo en una arquitectura popular para el desarrollo de software, permitiendo una mayor escalabilidad y flexibilidad.
        ''',
    )

    Article.objects.create(
        title='Desarrollo Ágil: Tendencias y Mejores Prácticas para 2024',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            El enfoque ágil sigue evolucionando, con nuevas prácticas y herramientas que optimizan la colaboración y la entrega continua de proyectos.
        ''',
    )

    Article.objects.create(
        title='El Papel de la Inteligencia Artificial en la Gestión de Proyectos',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            La inteligencia artificial está empezando a jugar un papel clave en la gestión de proyectos, ofreciendo análisis predictivo y automatización de tareas.
        ''',
    )

    Article.objects.create(
        title='Integración de la Realidad Virtual en la Educación Técnica',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            La realidad virtual se está utilizando cada vez más en la educación técnica, proporcionando experiencias inmersivas y prácticas para los estudiantes.
        ''',
    )

    Article.objects.create(
        title='El Desafío del Big Data: Nuevas Soluciones para el Manejo de Información',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            Con el crecimiento del big data, surgen nuevas soluciones y tecnologías para gestionar y analizar grandes volúmenes de información de manera eficiente.
        ''',
    )

    Article.objects.create(
        title='Innovaciones en el Desarrollo de Interfaces de Usuario',
        author=walter_hugo,
        featured_image='articles/fake_news.png',
        body='''
            Las últimas innovaciones en el desarrollo de interfaces de usuario están mejorando la accesibilidad y la experiencia general del usuario.
        ''',
    )

    Article.objects.create(
        title='Desarrollo de Software en el Contexto de la Economía Circular',
        featured_image='articles/fake_news.png',
        author=walter_hugo,
        body='''
            El concepto de economía circular está influyendo en el desarrollo de software, promoviendo prácticas que favorecen la sostenibilidad y la reducción de residuos.
        ''',
    )

    Article.objects.create(
        title='La Revolución de los Lenguajes de Programación Funcional',
        featured_image='articles/fake_news.png',
        author=walter_hugo,
        body='''
            Los lenguajes de programación funcional están ganando popularidad por sus beneficios en la gestión de la concurrencia y la simplicidad del código.
        ''',
    )

    Article.objects.create(
        title='Tendencias en el Desarrollo de Sistemas de Inteligencia Empresarial',
        featured_image='articles/fake_news.png',
        author=walter_hugo,
        body='''
            Las tendencias actuales en inteligencia empresarial están enfocadas en el uso de análisis avanzados y aprendizaje automático para tomar decisiones más informadas.
        ''',
    )

    Article.objects.create(
        title='El Impacto de la Automatización en el Desarrollo de Software Personalizado',
        featured_image='articles/fake_news.png',
        author=walter_hugo,
        body='''
            La automatización está facilitando la creación de software personalizado, permitiendo a las empresas adaptar soluciones a sus necesidades específicas con mayor rapidez.
        ''',
    )

    Article.objects.create(
        title='Estrategias para Optimizar el Rendimiento en el Desarrollo Web',
        featured_image='articles/fake_news.png',
        author=walter_hugo,
        body='''
            Optimizar el rendimiento web es crucial en la era digital actual, y las estrategias emergentes están ayudando a mejorar la velocidad y la eficiencia de los sitios web.
        ''',
    )

    Article.objects.create(
        title='Desarrollo de Aplicaciones Multiplataforma: Ventajas y Desafíos',
        featured_image='articles/fake_news.png',
        author=walter_hugo,
        body='''
            El desarrollo de aplicaciones multiplataforma ofrece ventajas significativas en términos de alcance y costos, pero también presenta desafíos en términos de compatibilidad y rendimiento.
        ''',
    )

    Article.objects.create(
        title='El Rol de los Chatbots en la Atención al Cliente',
        featured_image='articles/fake_news.png',
        author=walter_hugo,
        body='''
            Los chatbots están transformando la atención al cliente, proporcionando respuestas instantáneas y mejorando la eficiencia en la gestión de consultas y problemas.
        ''',
    )

    Article.objects.create(
        title='Nuevas Tendencias en el Desarrollo de Software para Dispositivos Wearables',
        featured_image='articles/fake_news.png',
        author=walter_hugo,
        body='''
            El desarrollo de software para dispositivos wearables está avanzando rápidamente, con nuevas tendencias que permiten una mayor integración y funcionalidad en dispositivos portátiles.
        ''',
    )

    # news fron LLWEB                                                         #
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

    article = Article(
        title='firma pre acuerdo LL',
        author=walter_hugo,
        featured_image='articles/firma_preacuerdo.jpeg',
        body='''
            Con gran entusiasmo seguimos celebrando la firma del pre acuerdo Nacional, un hito crucial en la construcción para nuestra agrupación. Este acuerdo, posibilta que Líderes Liberales llegue a la Provincia de Mendoza con nuestro referente Marcos Sanchez, también acompañó la firma la Diputada
            Mercedes Llano y Armando Maggistreti Presidente del PD de Mendoza. También tuvieron la oportunidad de firmar el pre acuerdo diversos miembros de CABA y PBA. La unión de líderes y miembros de diferentes regiones demuestra el compromiso compartido por la libertad. Este pre acuerdo es un testimonio de la creciente fuerza de nuestro movimiento, un movimiento que busca construir un legado.
        ''',
    )

    article.save()

    for i in range(10):
        Comment.objects.create(
            name=f'{i + 1}',
            email=f'{i + 1}@email.com',
            url=f'http://www.{i + 1}.com',
            message=f'message {i + 1}',
            article=article
        )

class Migration(migrations.Migration):
    dependencies=[
        ('press', '0001_initial'),
    ]

    operations=[
        migrations.RunPython(set_up),
    ]
