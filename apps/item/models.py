from django.db import models


# Create your models here.
class Item(models.Model):
	codigo = models.CharField(max_length=50)
	unidad = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=100)
	cantidad = models.IntegerField()
	pr_costo = models.IntegerField()

	def __unicode__(self):
		return self.descripcion
