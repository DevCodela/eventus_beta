# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_auto_20141003_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='tipo_pago',
            field=models.CharField(max_length=6, choices=[(b'gratis', b'Gratis'), (b'pago', b'Pago')]),
        ),
    ]
