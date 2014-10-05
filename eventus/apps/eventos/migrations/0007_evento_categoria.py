# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0006_auto_20141003_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='categoria',
            field=models.ForeignKey(default=1, to='eventos.Categoria'),
            preserve_default=False,
        ),
    ]
