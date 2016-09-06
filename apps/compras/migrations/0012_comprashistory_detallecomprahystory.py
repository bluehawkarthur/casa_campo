# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20160903_1725'),
        ('proveedor', '0003_remove_proveedor_grupos'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compras', '0011_auto_20160903_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprasHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comprobantetxt', models.CharField(max_length=15)),
                ('comprobante', models.IntegerField()),
                ('eliminado', models.BooleanField(default=False)),
                ('factura', models.IntegerField(null=True, blank=True)),
                ('fecha', models.DateField()),
                ('tipodcompra', models.CharField(max_length=50)),
                ('tipodcompra2', models.CharField(max_length=50)),
                ('grupo', models.CharField(max_length=100, null=True, blank=True)),
                ('total', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('fecha_accion', models.DateField()),
                ('proveedor', models.ForeignKey(blank=True, to='proveedor.Proveedor', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompraHystory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=50)),
                ('unidad', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('cantidad', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('pr_costo', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('compras', models.ForeignKey(blank=True, to='compras.Compras', null=True)),
                ('item', models.ForeignKey(blank=True, to='item.Item', null=True)),
            ],
        ),
    ]
