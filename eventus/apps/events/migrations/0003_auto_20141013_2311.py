# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20141013_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='resume',
            new_name='extract',
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.CharField(max_length=255),
        ),
    ]
