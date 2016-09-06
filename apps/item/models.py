from django.db import models


# Create your models here.
class Item(models.Model):
	codigo = models.CharField(max_length=50)
	unidad = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=100)
	cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	pr_costo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

	def __unicode__(self):
		return self.descripcion
