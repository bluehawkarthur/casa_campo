# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0002_auto_20160523_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='grupos',
        ),
    ]
