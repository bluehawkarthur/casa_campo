# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0005_auto_20160827_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='comprobantetxt',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='compras',
            name='eliminado',
            field=models.BooleanField(default=False),
        ),
    ]
