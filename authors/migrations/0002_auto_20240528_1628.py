# Generated by Django 3.2.25 on 2024-05-28 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='author',
            name='death_date',
        ),
    ]
