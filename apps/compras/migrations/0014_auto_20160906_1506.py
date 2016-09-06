# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0013_auto_20160906_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecomprahystory',
            name='compras',
            field=models.ForeignKey(blank=True, to='compras.ComprasHistory', null=True),
        ),
    ]
