# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20160903_1725'),
        ('proveedor', '0003_remove_proveedor_grupos'),
    ]

    operations = [
        migrations.CreateModel(
            name='KardexAlmacen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('tipo', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('pr_costo', models.IntegerField()),
                ('comprobantetxt', models.CharField(max_length=15)),
                ('comprobante', models.IntegerField()),
                ('factura', models.IntegerField(null=True, blank=True)),
                ('tipodcompra', models.CharField(max_length=50)),
                ('tipodcompra2', models.CharField(max_length=50)),
                ('grupo', models.CharField(max_length=100, null=True, blank=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('codigo', models.ForeignKey(blank=True, to='item.Item', null=True)),
                ('proveedor', models.ForeignKey(blank=True, to='proveedor.Proveedor', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KardexProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField()),
                ('fecha', models.DateField()),
                ('comprobantetxt', models.CharField(max_length=15)),
                ('comprobante', models.IntegerField()),
                ('monto', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('pagop_ar', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('factura', models.IntegerField(null=True, blank=True)),
                ('tipodcompra', models.CharField(max_length=50)),
                ('tipodcompra2', models.CharField(max_length=50)),
                ('cheque', models.CharField(max_length=100, null=True, blank=True)),
                ('banco', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
    ]
