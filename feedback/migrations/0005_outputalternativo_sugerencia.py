# Generated by Django 2.2.6 on 2020-05-26 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20200519_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='outputalternativo',
            name='sugerencia',
            field=models.TextField(blank=True, help_text='Sugerencia para la estudiante de como mejorar el código'),
        ),
    ]
