# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssistantEnrolled',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('attended', models.BooleanField(default=False)),
                ('has_paid', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Enrolled',
                'verbose_name_plural': 'Enrolled',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('resume', models.TextField(max_length=255)),
                ('content', models.TextField()),
                ('place', models.TextField(max_length=255)),
                ('start', models.DateTimeField()),
                ('finish', models.DateTimeField()),
                ('image', models.ImageField(upload_to=b'event_images')),
                ('payment_type', models.CharField(max_length=6, choices=[(b'gratis', b'Gratis'), (b'pago', b'Pago')])),
                ('amount', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('views', models.IntegerField(default=0, null=True, blank=True)),
                ('category', models.ForeignKey(to='events.Category')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=(models.Model,),
        ),
    ]
