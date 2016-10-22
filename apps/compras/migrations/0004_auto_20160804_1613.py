# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_compras_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='unidad',
            field=models.CharField(max_length=100),
        ),
    ]
