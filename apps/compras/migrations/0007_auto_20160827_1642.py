# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0006_auto_20160827_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='factura',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
