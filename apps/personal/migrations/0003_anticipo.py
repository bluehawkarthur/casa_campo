# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20160628_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anticipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anticipo', models.IntegerField()),
                ('fecha', models.DateField(null=True, blank=True)),
                ('codigo', models.ForeignKey(blank=True, to='personal.Personal', null=True)),
            ],
        ),
    ]
