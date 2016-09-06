# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0002_auto_20160523_1004'),
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='proveedor',
            field=models.ForeignKey(blank=True, to='proveedor.Proveedor', null=True),
        ),
    ]
