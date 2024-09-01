from django.db import migrations, models

from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from ..models import *


def set_up(apps, scheme_editor):
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

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % Groups                                                                %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Group.objects.create(name = 'BoardOfDirectorsGroups')
    Group.objects.create(name = 'MemberGroups')
    Group.objects.create(name = 'EditorGroups')

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % Users                                                                 %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    users = []

    users.append(
        BoardOfDirectors(
            username='antonio_garcia',
            first_name='Antonio',
            last_name='García',
            email='antonio_garcia@email.com',
            dni='77432035',
            province=Provinces.CABA,
            movil_phone='011 1234 5678',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        BoardOfDirectors(
            username='manuel_rodriguez',
            first_name='Manuel',
            last_name='Rodríguez',
            email='manuel_rodriguez@email.com',
            dni='67718011',
            province=Provinces.MENDOZA,
            movil_phone='0261 2345 6789',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(

        BoardOfDirectors(
            username='francisco_gonzalez',
            first_name='Francisco',
            last_name='González',
            email='francisco_gonzalez@email.com',
            dni='96035688',
            province=Provinces.CHACO,
            movil_phone='0362 2345 6789',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(

        BoardOfDirectors(
            username='jose_fernandez',
            first_name='José',
            last_name='Fernández',
            email='jose_fernandez@email.com',
            dni='61070632',
            province=Provinces.CABA,
            movil_phone='011 9876 5432',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(

        BoardOfDirectors(
            username='david_lopez',
            first_name='David',
            last_name='López',
            email='david_lopez@email.com',
            dni='75699394',
            province=Provinces.JUJUY,
            movil_phone='0388 2345 6789',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(

        BoardOfDirectors(
            username='maria_perez',
            first_name='María',
            last_name='Pérez',
            email='maria_perez@email.com',
            dni='43778414',
            province=Provinces.SANTA_FE,
            movil_phone='0342 2345 6789',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(

        BoardOfDirectors(
            username='carmen_martinez',
            first_name='Carmen',
            last_name='Martínez',
            email='carmen_martinez@email.com',
            dni='56661163',
            province=Provinces.CORDOBA,
            movil_phone='0351 2345 6789',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        BoardOfDirectors(
            username='isabel_sanchez',
            first_name='Isabel',
            last_name='Sánchez',
            email='isabel_sanchez@email.com',
            dni='44618761',
            province=Provinces.FORMOSA,
            movil_phone='0370 2345 6789',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        BoardOfDirectors(
            username='laura_gomez',
            first_name='Laura',
            last_name='Gómez',
            email='laura_gomez@email.com',
            dni='55066973',
            province=Provinces.BUENOS_AIRES,
            movil_phone='0234 5678 1234',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        BoardOfDirectors(
            username='ana_vazquez',
            first_name='Ana',
            last_name='Vázquez',
            email='ana_vazquez@email.com',
            dni='61444894',
            province=Provinces.SAN_JUAN,
            movil_phone='0264 5678 1234',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Member(
            username='juan_morales',
            first_name='Juan',
            last_name='Morales',
            email='juan_morales@email.com',
            dni='35146365',
            province=Provinces.CORRIENTES,
            movil_phone='0378 2345 6789',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Member(
            username='javier_romero',
            first_name='Javier',
            last_name='Romero',
            email='javier_romero@email.com',
            dni='20078096',
            province=Provinces.SANTA_FE,
            movil_phone='0342 9876 5432',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Member(
            username='daniel_jimenez',
            first_name='Daniel',
            last_name='Jiménez',
            email='daniel_jimenez@email.com',
            dni='88556295',
            province=Provinces.CATAMARCA,
            movil_phone='0383 2345 6789',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Member(
            username='miguel_mendoza',
            first_name='Miguel',
            last_name='Mendoza',
            email='miguel_mendoza@email.com',
            dni='84334857',
            province=Provinces.BUENOS_AIRES,
            movil_phone='011 5678 1234',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Member(
            username='carlos_castro',
            first_name='Carlos',
            last_name='Castro',
            email='carlos_castro@email.com',
            dni='81634137',
            province=Provinces.LA_PAMPA,
            movil_phone='02954 2345 6789',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Member(
            username='dolores_hernandez',
            first_name='Dolores',
            last_name='Hernández',
            email='dolores_hernandez@email.com',
            dni='46665008',
            province=Provinces.CHACO,
            movil_phone='0362 6789 1234',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Member(
            username='rosa_jimenez',
            first_name='Rosa',
            last_name='Jiménez',
            email='rosa_jimenez@email.com',
            dni='39520613',
            province=Provinces.RIO_NEGRO,
            movil_phone='02954 6789 1234',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Member(
            username='teresa_rivera',
            first_name='Teresa',
            last_name='Rivera',
            email='teresa_rivera@email.com',
            dni='47239355',
            province=Provinces.SANTIAGO_DEL_ESTERO,
            movil_phone='0385 2345 6789',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Member(
            username='pilar_ramos',
            first_name='Pilar',
            last_name='Ramos',
            email='pilar_ramos@email.com',
            dni='84800515',
            province=Provinces.SANTA_CRUZ,
            movil_phone='02966 2345 6789',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Member(
            username='marta_alvarez',
            first_name='Marta',
            last_name='Alvarez',
            email='marta_alvarez@email.com',
            dni='55757440',
            province=Provinces.CABA,
            movil_phone='011 8765 4321',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Editor(
            username='francisco_javier_cruz',
            first_name='Francisco Javier',
            last_name='Cruz',
            email='francisco_javier_cruz@email.com',
            dni='54605973',
            province=Provinces.SAN_LUIS,
            movil_phone='0266 9876 5432',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Editor(
            username='alejandro_ortiz',
            first_name='Alejandro',
            last_name='Ortiz',
            email='alejandro_ortiz@email.com',
            dni='56206933',
            province=Provinces.MISIONES,
            movil_phone='0376 2345 6789',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Editor(
            username='sergio_diaz',
            first_name='Sergio',
            last_name='Díaz',
            email='sergio_diaz@email.com',
            dni='31181102',
            province=Provinces.CHUBUT,
            movil_phone='0299 2345 6789',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Editor(
            username='rafael_guerrero',
            first_name='Rafael',
            last_name='Guerrero',
            email='rafael_guerrero@email.com',
            dni='57455635',
            province=Provinces.SANTIAGO_DEL_ESTERO,
            movil_phone='0385 6789 1234',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Editor(
            username='francisco_jose_moreno',
            first_name='Francisco José',
            last_name='Moreno',
            email='francisco_jose_moreno@email.com',
            dni='41618675',
            province=Provinces.CABA,
            movil_phone='011 1234 8765',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Editor(
            username='nuria_luna',
            first_name='Nuria',
            last_name='Luna',
            email='nuria_luna@email.com',
            dni='60187385',
            province=Provinces.SALTA,
            movil_phone='0370 9876 5432',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Editor(
            username='eva_salazar',
            first_name='Eva',
            last_name='Salazar',
            email='eva_salazar@email.com',
            dni='96351776',
            province=Provinces.LA_RIOJA,
            movil_phone='0380 2345 6789',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Editor(
            username='patricia_valdez',
            first_name='Patricia',
            last_name='Valdez',
            email='patricia_valdez@email.com',
            dni='72970491',
            province=Provinces.TUCUMAN,
            movil_phone='0381 2345 6789',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Editor(
            username='beatriz_torres',
            first_name='Beatriz',
            last_name='Torres',
            email='beatriz_torres@email.com',
            dni='63782765',
            province=Provinces.CABA,
            movil_phone='011 4567 8901',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    users.append(
        Editor(
            username='julia_paniagua',
            first_name='Julia',
            last_name='Paniagua',
            email='julia_paniagua@email.com',
            dni='93986590',
            province=Provinces.RIO_NEGRO,
            movil_phone='02954 6789 2345',
            is_superuser=False,
            is_staff=True,
            is_active=True
        ))

    for user in users:
        user.set_password('1234')
        user.save()


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(set_up),
    ]