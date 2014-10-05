# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_auto_20141003_2243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categor\xeda', 'verbose_name_plural': 'Categor\xedas'},
        ),
        migrations.AlterModelOptions(
            name='comentario',
            options={'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentarios'},
        ),
        migrations.AlterModelOptions(
            name='evento',
            options={'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
        migrations.AlterModelOptions(
            name='tickets',
            options={'verbose_name': 'Ticket', 'verbose_name_plural': 'Tickets'},
        ),
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(editable=False),
        ),
        migrations.AlterField(
            model_name='evento',
            name='contenido',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_inicio',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_termino',
            field=models.DateField(),
        ),
    ]
