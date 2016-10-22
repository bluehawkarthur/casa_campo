from django.db import models
from apps.item.models import Item
from apps.proveedor.models import Proveedor
from django.conf import settings


# Create your models here.
class Compras(models.Model):
	comprobantetxt = models.CharField(max_length=15)
	comprobante = models.IntegerField()
	eliminado = models.BooleanField(default=False)
	factura = models.IntegerField(null=True, blank=True)
	fecha = models.DateField()
	tipodcompra = models.CharField(max_length=50)
	tipodcompra2 = models.CharField(max_length=50)
	grupo = models.CharField(max_length=100, null=True, blank=True)
	total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	proveedor = models.ForeignKey(Proveedor, null=True, blank=True)

	def __unicode__(self):
		return U" %s- %s" % (self.comprobante, self.factura)



class DetalleCompra(models.Model):
	codigo = models.CharField(max_length=50)
	unidad = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	pr_costo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	compras = models.ForeignKey(Compras, null=True, blank=True)
	item = models.ForeignKey(Item, null=True, blank=True)

	def __unicode__(self):
		return U" %s- %s" % (self.compras.comprobante, self.descripcion)


# Create your models here.
class ComprasHistory(models.Model):
	comprobantetxt = models.CharField(max_length=15)
	comprobante = models.IntegerField()
	eliminado = models.BooleanField(default=False)
	factura = models.IntegerField(null=True, blank=True)
	fecha = models.DateField()
	tipodcompra = models.CharField(max_length=50)
	tipodcompra2 = models.CharField(max_length=50)
	grupo = models.CharField(max_length=100, null=True, blank=True)
	total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	proveedor = models.ForeignKey(Proveedor, null=True, blank=True)
	fecha_accion = models.DateField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)

	def __unicode__(self):
		return U" %s- %s" % (self.comprobante, self.factura)


class DetalleCompraHystory(models.Model):
	codigo = models.CharField(max_length=50)
	unidad = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	pr_costo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	compras = models.ForeignKey(ComprasHistory, null=True, blank=True)
	item = models.ForeignKey(Item, null=True, blank=True)

	def __unicode__(self):
		return U" %s- %s" % (self.codigo, self.descripcion)

