# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0003_auto_20141003_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('ha_pagado', models.BooleanField(default=False)),
                ('asistente', models.ForeignKey(related_name=b'asistente', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('evento', models.ForeignKey(blank=True, to='eventos.Evento', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='inscritos',
            name='asistente',
        ),
        migrations.RemoveField(
            model_name='inscritos',
            name='evento',
        ),
        migrations.DeleteModel(
            name='Inscritos',
        ),
        migrations.AddField(
            model_name='evento',
            name='inscritos',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='eventos.Tickets'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='organizador',
            field=models.ForeignKey(related_name=b'organizador', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
