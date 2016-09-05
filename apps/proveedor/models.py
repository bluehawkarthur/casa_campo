from django.db import models


# Create your models here.
class Proveedor(models.Model):
	codigo = models.CharField(max_length=100)
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return U" %s- %s" % (self.codigo, self.nombre)
	