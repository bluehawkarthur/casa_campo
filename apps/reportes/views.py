from django.shortcuts import render
from pure_pagination.mixins import PaginationMixin
from django.views.generic import ListView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from .models import KardexAlmacen

class ListarKardexAlmacen(PaginationMixin, ListView):
	template_name = 'reportes/listar_kalm.html'
	paginate_by = 5
	model = KardexAlmacen
	context_object_name = 'kalm'


class EditKardexAlmacen(UpdateView):
	template_name = 'reportes/edit_kalm.html'
	model = KardexAlmacen
	fields = ['codigo', 'fecha', 'tipo', 'cantidad', 'pr_costo', 'comprobantetxt', 'factura', 'proveedor', 'grupo']
	success_url = reverse_lazy('lista_kalm')


def DeleteKalm(request, kar):
	e = KardexAlmacen.objects.get(id=kar)
	e.delete()
	return HttpResponseRedirect(reverse_lazy('lista_kalm'))
