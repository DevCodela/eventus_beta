# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('descripcion', models.CharField(unique=True, max_length=50)),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('contenido', models.TextField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(unique=True, max_length=200)),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('resumen', models.TextField(max_length=255)),
                ('contenido', models.TextField(max_length=255)),
                ('lugar', models.TextField(max_length=255)),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('fecha_termino', models.DateTimeField(auto_now_add=True)),
                ('hora_inicio', models.TimeField()),
                ('hora_termino', models.TimeField()),
                ('imagen', models.ImageField(upload_to=b'imagenes')),
                ('tipo_pago', models.CharField(max_length=5, choices=[(b'gratis', b'Gratis'), (b'pago', b'Pago')])),
                ('monto', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('visitas', models.IntegerField(default=0, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inscritos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
