# Generated by Django 5.0.3 on 2024-03-21 18:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_initial'),
        ('participation', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ColumnModel',
            new_name='ParticipationModel',
        ),
    ]
