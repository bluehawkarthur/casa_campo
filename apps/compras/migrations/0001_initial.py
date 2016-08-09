# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comprobante', models.IntegerField()),
                ('factura', models.IntegerField()),
                ('fecha', models.DateField()),
                ('tipodcompra', models.CharField(max_length=50)),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=50)),
                ('unidad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('pr_costo', models.IntegerField()),
                ('compras', models.ForeignKey(blank=True, to='compras.Compras', null=True)),
                ('item', models.ForeignKey(blank=True, to='item.Item', null=True)),
            ],
        ),
    ]
