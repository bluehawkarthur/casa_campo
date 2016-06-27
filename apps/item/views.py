from django.shortcuts import render_to_response, render
from django.views.generic import FormView, ListView, DetailView, UpdateView
from pure_pagination.mixins import PaginationMixin
from django.core.urlresolvers import reverse_lazy
from .forms import ItemForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import Item


# Create your views here. , UpdateView, DeleteView
def CrearItem(request):
	if request.method == 'POST':
		form = ItemForm(request.POST)
		if form.is_valid():
			item = Item(
				codigo=form.cleaned_data['codigo'],
				unidad=form.cleaned_data['unidad'],
				descripcion=form.cleaned_data['descripcion'],
				cantidad=form.cleaned_data['cantidad'],
				pr_costo=form.cleaned_data['pr_costo'])
			item.save()
			return HttpResponseRedirect(reverse_lazy('listar_item'))
	else:
		print 'dfsdfsdfsdf'
		form = ItemForm()

	variables = RequestContext(request, {'form': form})
	return render_to_response('item/crearitem.html', variables)


class ListarItem(PaginationMixin, ListView):
	template_name = 'item/listar_item.html'
	paginate_by = 5
	model = Item
	context_object_name = 'item'


class DetalleItem(DetailView):
	template_name = 'item/detalle_item.html'
	model = Item
	context_object_name = 'item'


class EditItem(UpdateView):
	template_name = 'item/edit_item.html'
	model = Item
	fields = ['codigo', 'unidad', 'descripcion', 'cantidad', 'pr_costo']
	success_url = reverse_lazy('listar_item')


def DeleteItem(request, item):
	e = Item.objects.get(id=item)
	e.delete()
	return HttpResponseRedirect(reverse_lazy('listar_item'))