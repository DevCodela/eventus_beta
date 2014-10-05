# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20141003_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='descripcion',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='titulo',
            new_name='nombre',
        ),
    ]
