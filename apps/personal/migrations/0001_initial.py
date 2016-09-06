# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=50)),
                ('porcentaje', models.DecimalField(max_digits=2, decimal_places=2)),
                ('tipo', models.CharField(max_length=2)),
            ],
        ),
    ]
