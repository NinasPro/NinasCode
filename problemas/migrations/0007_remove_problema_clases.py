# Generated by Django 2.2.13 on 2020-06-09 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problemas', '0006_problema_clases'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problema',
            name='clases',
        ),
    ]