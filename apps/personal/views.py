from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, UpdateView, TemplateView
from django.core import serializers
from django.http import HttpResponse
from datetime import date, datetime
import datetime

from .forms import PersonalForm, AnticipoForm
from .models import Personal, Anticipo



def crearPersonal(request):
	if request.method == 'POST':
		form = PersonalForm(request.POST)
		if form.is_valid():
			personal = Personal(
				codigo = form.cleaned_data['codigo'],
				nombre = form.cleaned_data['nombre'],
				porcentaje = form.cleaned_data['porcentaje'],
				tipo = form.cleaned_data['tipo']
				)
			personal.save()
			return HttpResponseRedirect(reverse_lazy('listar_personal'))
	else:
		form = PersonalForm
	variables = RequestContext(request, {'form': form})
	return render_to_response('personal/crear_personal.html', variables)


class ListarPersonal(ListView):
	template_name = 'personal/listar_personal.html'
	#paginate_by = 5
	model = Personal
	context_object_name = 'personal'


class EditPersonal(UpdateView):
	template_name = 'personal/edit_personal.html'
	model = Personal
	fields = ['codigo', 'nombre', 'porcentaje', 'tipo']
	success_url = reverse_lazy('listar_personal')


def deletePersonal(request, id):
	e = Personal.objects.get(id=id)
	e.delete()
	return HttpResponseRedirect(reverse_lazy('listar_personal'))


# -------------------------- ANTICPOS -----------------------

class ListarAnticipo(ListView):
	template_name = 'personal/listar_anticipos.html'
	queryset = Anticipo.objects.order_by('-fecha')
	#paginate_by = 5
	model = Anticipo
	context_object_name = 'anticipo'

	

def crearAnticipo(request):
	if request.method == 'POST':
		form = AnticipoForm(request.POST)
		print 'FORMMMMMMMM', form
		if form.is_valid():
			date_1 = datetime.datetime.strptime(request.POST['fecha'], '%d/%m/%Y').strftime("%Y-%m-%d")
			ant = Anticipo()
			ant.codigo = form.cleaned_data['codigo']
			ant.anticipo = form.cleaned_data['anticipo']
			ant.fecha = date_1
			ant.save()
			return HttpResponseRedirect(reverse_lazy('listar_anticipos'))
	else:
		form = AnticipoForm
	variables = RequestContext(request, {'form': form})
	return render_to_response('personal/crear_anticipo.html', variables)


class BusquedaPersonal(TemplateView):

	def get(self, request, *args, **kwargs):
		id_personal = request.GET['id']
		#print 'gfsdhfgjsdgfsdfjhsdgf', id_personal
		personal = Personal.objects.filter(id=id_personal)
		data = serializers.serialize('json', personal)
		#print 'DATATATATTATAT', data
		return HttpResponse(data, content_type='application/json')


class EditAnticipo(UpdateView):
	template_name = 'personal/edit_anticipo.html'
	model = Anticipo
	fields = ['codigo', 'anticipo', 'fecha']
	success_url = reverse_lazy('listar_anticipos')


class BusquedaNombre(TemplateView):
	def get(self, request, *args, **kwargs):
		cod = request.GET['cod2']
		print 'RECIBE EL CODIGO', cod
		personal = Personal.objects.filter(codigo=cod)
		data = serializers.serialize('json', personal)
		print 'DATATATATTATAT', data
		return HttpResponse(data, content_type='application/json')


def deleteAnticipo(request, id):
	e = Anticipo.objects.get(id=id)
	e.delete()
	return HttpResponseRedirect(reverse_lazy('listar_anticipos'))