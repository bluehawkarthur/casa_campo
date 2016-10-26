from django import forms


class ProveedorForm(forms.Form):
	codigo = forms.CharField(max_length=100)
	nombre = forms.CharField(max_length=100)