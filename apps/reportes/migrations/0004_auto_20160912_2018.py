# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0003_auto_20160912_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kardexalmacen',
            name='cantidad',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='kardexalmacen',
            name='pr_costo',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
