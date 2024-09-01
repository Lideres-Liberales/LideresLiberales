# Generated by Django 5.0.7 on 2024-08-18 17:19

import django.core.validators
import django.db.models.deletion
import public.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticalParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.CharField(max_length=100, verbose_name='Denominacion')),
                ('color', models.CharField(max_length=9, verbose_name='Color (en hexadecimal)')),
            ],
            options={
                'verbose_name': 'Partido Politico',
                'verbose_name_plural': 'Partidos Politicos',
                'db_table': 'public_political_parties',
            },
        ),
        migrations.CreateModel(
            name='ExecutiveBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('position', models.CharField(max_length=100, verbose_name='Cargo')),
                ('avatar_image', models.ImageField(upload_to='functionaries/avatar', verbose_name='Foto Avatar')),
                ('perfil_image', models.ImageField(upload_to='functionaries/profile', verbose_name='Foto Perfil')),
                ('biography', models.TextField(blank=True, null=True, verbose_name='Biografia')),
                ('height', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nivel')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='team_members', to='public.executivebranch', verbose_name='Superior')),
                ('political_party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_political_party', to='public.politicalparty', verbose_name='Partido Politico')),
            ],
            options={
                'verbose_name': 'Miembro poder ejecutivo',
                'verbose_name_plural': 'Miembros poder ejecutivo',
                'db_table': 'public_executive_branch',
            },
            bases=(models.Model, public.models.ImageDeletionMixin),
        ),
        migrations.CreateModel(
            name='Deputie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('position', models.CharField(max_length=100, verbose_name='Cargo')),
                ('avatar_image', models.ImageField(upload_to='functionaries/avatar', verbose_name='Foto Avatar')),
                ('perfil_image', models.ImageField(upload_to='functionaries/profile', verbose_name='Foto Perfil')),
                ('biography', models.TextField(blank=True, null=True, verbose_name='Biografia')),
                ('is_president', models.BooleanField(default=False, verbose_name='Presidente de camara')),
                ('political_party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_political_party', to='public.politicalparty', verbose_name='Partido Politico')),
            ],
            options={
                'verbose_name': 'Diputado',
                'verbose_name_plural': 'Diputados',
                'db_table': 'public_deputie',
            },
            bases=(models.Model, public.models.ImageDeletionMixin),
        ),
        migrations.CreateModel(
            name='Councillor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('position', models.CharField(max_length=100, verbose_name='Cargo')),
                ('avatar_image', models.ImageField(upload_to='functionaries/avatar', verbose_name='Foto Avatar')),
                ('perfil_image', models.ImageField(upload_to='functionaries/profile', verbose_name='Foto Perfil')),
                ('biography', models.TextField(blank=True, null=True, verbose_name='Biografia')),
                ('municipality', models.CharField(max_length=100, verbose_name='Municipio')),
                ('political_party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_political_party', to='public.politicalparty', verbose_name='Partido Politico')),
            ],
            options={
                'verbose_name': 'Consejal',
                'verbose_name_plural': 'Consejales',
                'db_table': 'public_councillor',
            },
            bases=(models.Model, public.models.ImageDeletionMixin),
        ),
        migrations.CreateModel(
            name='CommunityBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('position', models.CharField(max_length=100, verbose_name='Cargo')),
                ('avatar_image', models.ImageField(upload_to='functionaries/avatar', verbose_name='Foto Avatar')),
                ('perfil_image', models.ImageField(upload_to='functionaries/profile', verbose_name='Foto Perfil')),
                ('biography', models.TextField(blank=True, null=True, verbose_name='Biografia')),
                ('commune', models.CharField(max_length=100, verbose_name='Comuna')),
                ('political_party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_political_party', to='public.politicalparty', verbose_name='Partido Politico')),
            ],
            options={
                'verbose_name': 'Miembro junta comunal',
                'verbose_name_plural': 'Miembros junta comunal',
                'db_table': 'public_community_board',
            },
            bases=(models.Model, public.models.ImageDeletionMixin),
        ),
        migrations.CreateModel(
            name='Senator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('position', models.CharField(max_length=100, verbose_name='Cargo')),
                ('avatar_image', models.ImageField(upload_to='functionaries/avatar', verbose_name='Foto Avatar')),
                ('perfil_image', models.ImageField(upload_to='functionaries/profile', verbose_name='Foto Perfil')),
                ('biography', models.TextField(blank=True, null=True, verbose_name='Biografia')),
                ('political_party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_political_party', to='public.politicalparty', verbose_name='Partido Politico')),
            ],
            options={
                'verbose_name': 'Senador',
                'verbose_name_plural': 'Senadores',
                'db_table': 'public_senator',
            },
            bases=(models.Model, public.models.ImageDeletionMixin),
        ),
    ]
