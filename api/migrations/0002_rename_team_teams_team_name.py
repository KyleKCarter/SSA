# Generated by Django 5.1.5 on 2025-01-15 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teams',
            old_name='team',
            new_name='team_name',
        ),
    ]
