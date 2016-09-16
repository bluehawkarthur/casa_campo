# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0014_auto_20160906_1506'),
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kardexalmacen',
            name='compra',
            field=models.ForeignKey(blank=True, to='compras.Compras', null=True),
        ),
    ]
