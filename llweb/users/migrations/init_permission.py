from django.db import migrations
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.sql import emit_post_migrate_signal

from ..models import *


def set_up(apps, schema_editor):
    emit_post_migrate_signal(0, False, 'default')

    Group.objects.get(name='BoardOfDirectorsGroups').permissions.set(
        Permission.objects.filter(codename__in=['view_profile', 'view_boardofdirectors'])
    )

    Group.objects.get(name='MemberGroups').permissions.set(
        Permission.objects.filter(codename__in=['view_profile', 'view_member'])
    )

    Group.objects.get(name='EditorGroups').permissions.set(
        Permission.objects.filter(codename__in=['view_profile', 'view_editor'])
    )


class Migration(migrations.Migration):
    dependencies = [
        ('users', 'init_database'),
    ]

    operations = [
        migrations.RunPython(set_up),
    ]