from django.db import models

class Personal(models.Model):
	codigo = models.CharField(max_length=5)
	nombre = models.CharField(max_length=50)
	porcentaje = models.DecimalField(max_digits=4, decimal_places=2)
	tipo = models.CharField(max_length=2)


	def __unicode__(self):
		return self.codigo


class Anticipo(models.Model):
	codigo = models.ForeignKey(Personal, null=True, blank=True)
	anticipo = models.IntegerField()
	fecha = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return U"%s - %s - %s" % (self.codigo, self.codigo.nombre, self.anticipo)