from django.db import models
from apps.item.models import Item
from apps.proveedor.models import Proveedor


# Create your models here.
class Compras(models.Model):
	comprobante = models.IntegerField()
	factura = models.IntegerField()
	fecha = models.DateField()
	tipodcompra = models.CharField(max_length=50)
	grupo = models.CharField(max_length=100, null=True, blank=True)
	total = models.IntegerField()
	proveedor = models.ForeignKey(Proveedor, null=True, blank=True)

	def __unicode__(self):
		return U" %s- %s" % (self.comprobante, self.factura)



class DetalleCompra(models.Model):
	codigo = models.CharField(max_length=50)
	unidad = models.IntegerField()
	descripcion = models.CharField(max_length=100)
	cantidad = models.IntegerField()
	pr_costo = models.IntegerField()
	compras = models.ForeignKey(Compras, null=True, blank=True)
	item = models.ForeignKey(Item, null=True, blank=True)
