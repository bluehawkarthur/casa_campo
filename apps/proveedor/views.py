from django.shortcuts import render_to_response, render
from django.views.generic import FormView, ListView, DetailView, UpdateView
from pure_pagination.mixins import PaginationMixin
from django.core.urlresolvers import reverse_lazy
from .forms import ProveedorForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import Proveedor


# Create your views here. , UpdateView, DeleteView
def CrearProveedor(request):
	if request.method == 'POST':
		form = ProveedorForm(request.POST)
		if form.is_valid():
			proveedor = Proveedor(
				codigo=form.cleaned_data['codigo'],
				nombre=form.cleaned_data['nombre'],
				grupos=form.cleaned_data['grupos'])
			proveedor.save()
			return HttpResponseRedirect(reverse_lazy('listar_proveed'))
	else:
		print 'dfsdfsdfsdf'
		form = ProveedorForm()

	variables = RequestContext(request, {'form': form})
	return render_to_response('proveedor/crear_proveed.html', variables)


class ListarProvedor(PaginationMixin, ListView):
	template_name = 'proveedor/listar_proveed.html'
	paginate_by = 5
	model = Proveedor
	context_object_name = 'proveedor'


class DetalleProveedor(DetailView):
	template_name = 'proveedor/detalle_proveed.html'
	model = Proveedor
	context_object_name = 'proveedor'


class EditProveedor(UpdateView):
	template_name = 'proveedor/edit_prove.html'
	model = Proveedor
	fields = ['codigo', 'nombre', 'grupos']
	success_url = reverse_lazy('listar_proveed')


def DeleteProveedor(request, proveedor):
	e = Proveedor.objects.get(id=proveedor)
	e.delete()
	return HttpResponseRedirect(reverse_lazy('listar_proveed'))