from django import forms



class ComprasForm(forms.Form):
	comprobante = forms.IntegerField()
	factura = forms.IntegerField()
	fecha = forms.DateField()
	tipodcompra = forms.CharField(max_length=50)
	total = forms.IntegerField()


class DetalleCompraForm(forms.Form):
	codigo = forms.CharField(max_length=50)
	unidad = forms.IntegerField()
	descripcion = forms.CharField(max_length=100)
	cantidad = forms.IntegerField()
	pr_costo = forms.IntegerField()
	compras = forms.ForeignKey(Compras, null=True, blank=True)
	item = forms.ForeignKey(Item, null=True, blank=True)