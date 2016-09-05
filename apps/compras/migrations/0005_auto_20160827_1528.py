# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_auto_20160804_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='eliminado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='compras',
            name='tipodcompra2',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
