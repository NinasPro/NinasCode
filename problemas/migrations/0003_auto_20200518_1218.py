# Generated by Django 2.2.6 on 2020-05-18 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problemas', '0002_caso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caso',
            old_name='descripcion',
            new_name='categoría',
        ),
    ]