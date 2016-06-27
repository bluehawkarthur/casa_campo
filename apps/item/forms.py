from django import forms


class ItemForm(forms.Form):
	codigo = forms.CharField(max_length=50)
	unidad = forms.IntegerField()
	descripcion = forms.CharField(max_length=100)
	cantidad = forms.IntegerField()
	pr_costo = forms.IntegerField()