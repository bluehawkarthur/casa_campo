# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0004_proveedor_saldo'),
        ('reportes', '0004_auto_20160912_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kardexproveedor',
            old_name='monto',
            new_name='deuda',
        ),
        migrations.RenameField(
            model_name='kardexproveedor',
            old_name='tipodcompra',
            new_name='forma_pago',
        ),
        migrations.RenameField(
            model_name='kardexproveedor',
            old_name='pagop_ar',
            new_name='pago',
        ),
        migrations.RemoveField(
            model_name='kardexproveedor',
            name='banco',
        ),
        migrations.RemoveField(
            model_name='kardexproveedor',
            name='cheque',
        ),
        migrations.RemoveField(
            model_name='kardexproveedor',
            name='factura',
        ),
        migrations.RemoveField(
            model_name='kardexproveedor',
            name='hora',
        ),
        migrations.RemoveField(
            model_name='kardexproveedor',
            name='tipodcompra2',
        ),
        migrations.AddField(
            model_name='kardexproveedor',
            name='proveedor',
            field=models.ForeignKey(blank=True, to='proveedor.Proveedor', null=True),
        ),
    ]
