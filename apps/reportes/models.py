from django.db import models
from apps.item.models import Item
from apps.proveedor.models import Proveedor


class KardexAlmacen(models.Model):
	codigo = models.ForeignKey(Item, null=True, blank=True)
	fecha = models.DateField()
	tipo = models.IntegerField() # Para indentificar al tipo de movimiento ej: compra, venta
	cantidad = models.IntegerField()
	pr_costo = models.IntegerField()
	comprobantetxt = models.CharField(max_length=15)
	comprobante = models.IntegerField()
	factura = models.IntegerField(null=True, blank=True)
	tipodcompra = models.CharField(max_length=50)
	tipodcompra2 = models.CharField(max_length=50)
	grupo = models.CharField(max_length=100, null=True, blank=True)
	proveedor = models.ForeignKey(Proveedor, null=True, blank=True)
	hora = models.TimeField(auto_now_add=True, blank=True)

	def __unicode__(self):
		return U" %s - %s - %s - %s" % (self.comprobante, self.tipo, self.factura, self.hora)


class KardexProveedor(models.Model):
	tipo = models.IntegerField() # Para indentificar al tipo de movimiento ej: compra, venta
	fecha = models.DateField()
	comprobantetxt = models.CharField(max_length=15)
	comprobante = models.IntegerField()
	monto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	pagop_ar = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	hora = models.TimeField(auto_now_add=True, blank=True)
	factura = models.IntegerField(null=True, blank=True)
	tipodcompra = models.CharField(max_length=50)
	tipodcompra2 = models.CharField(max_length=50)
	cheque = models.CharField(max_length=100, null=True, blank=True)
	banco = models.CharField(max_length=100, null=True, blank=True)

	def __unicode__(self):
		return U" %s - %s - %s - %s" % (self.comprobante, self.tipo, self.factura, self.hora)
