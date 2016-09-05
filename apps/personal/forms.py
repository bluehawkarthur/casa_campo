from django import forms
from .models import Personal

class PersonalForm(forms.Form):
    codigo = forms.CharField(max_length=5)
    nombre = forms.CharField(max_length=50)
    porcentaje = forms.DecimalField(max_digits=5, decimal_places=2)
    tipo = forms.CharField(max_length=2)


class AnticipoForm(forms.Form):
    codigo = forms.ModelChoiceField(queryset=Personal.objects.all())
    nombre = forms.CharField()
    anticipo = forms.IntegerField()
    fecha = forms.DateField()


