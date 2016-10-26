# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0003_remove_proveedor_grupos'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='saldo',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
