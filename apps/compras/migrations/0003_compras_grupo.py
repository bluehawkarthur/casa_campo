# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_compras_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='grupo',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
