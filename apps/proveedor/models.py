from django.db import models


# Create your models here.
class Proveedor(models.Model):
	codigo = models.CharField(max_length=100)
	nombre = models.CharField(max_length=100)
	saldo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

	def __unicode__(self):
		return U" %s- %s" % (self.codigo, self.nombre)
	