from django.shortcuts import render
from pure_pagination.mixins import PaginationMixin
from django.views.generic import ListView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from .models import KardexAlmacen
from apps.compras.models import Compras, DetalleCompra
from apps.item.models import Item
from django.template import RequestContext as ctx
from django.http import HttpResponse
from .excel_compras import WriteToCompras
from .excel_inventario import WriteToInventario
from django.contrib import messages
import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal, ROUND_HALF_UP


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


def ReporteCompras(request):

    template_name = "reportes/reporte_compras.html"
    town = None

    if request.method == 'POST':
        fecha_de = request.POST['fecha_de']
        fecha_a = request.POST['fecha_a']
        grupo = request.POST['grupo']
        tipo_compra = request.POST['pago']

        if tipo_compra == '':
        	if grupo != '':
        		compracabezera = Compras.objects.filter(fecha__range=(fecha_de, fecha_a), grupo=grupo).order_by('fecha')
        	else:
        		compracabezera = Compras.objects.filter(fecha__range=(fecha_de, fecha_a)).order_by('fecha')
        else:
        	if grupo != '':
        		compracabezera = Compras.objects.filter(fecha__range=(fecha_de, fecha_a), grupo=grupo, tipodcompra=tipo_compra).order_by('fecha')
        	else:
        		compracabezera = Compras.objects.filter(fecha__range=(fecha_de, fecha_a), tipodcompra=tipo_compra).order_by('fecha')

        vd = []
        for cab in compracabezera:
        	det = DetalleCompra.objects.filter(compras=cab.pk)
        	for d in det:
        		vd.append({
	            	'codigo': d.codigo,
	            	'descripcion': d.descripcion,
	            	'unidad': d.unidad,
	            	'cantidad': d.cantidad,
	            	'pr_costo': d.pr_costo,
	            	'total_compra': d.cantidad*d.pr_costo,
	            	'comprobantetxt': d.compras.comprobantetxt,
	            	'fecha': d.compras.fecha,
	            	'factura': d.compras.factura
	            })

        	vd.append({
            	'codigo': '',
            	'descripcion': 'Total Comp.',
            	'unidad': '',
            	'cantidad': '',
            	'pr_costo': '',
            	'total_compra': cab.total,
            	'comprobantetxt': '-------',
            	'fecha': '',
            	'factura': 0
            })

        print vd
        # try:
    	# obteniendo datos del modelo venta
    	# compras = DetalleCompra.objects.filter(compras__fecha__range=(fecha_de, fecha_a)).order_by('compras__fecha')
    	
    	# total = 0
     #    for c in compras:
     #        total = total + 1
            # total += compra.compras.total

        data_de = datetime.datetime.strptime(str(fecha_de), '%Y-%m-%d').strftime("%d/%m/%Y")
        data_a = datetime.datetime.strptime(str(fecha_a), '%Y-%m-%d').strftime("%d/%m/%Y")


        if 'excel' in request.POST:
            response = HttpResponse(content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=libro_ventas.xlsx'
            xlsx_data = WriteToCompras(vd, data_de, data_a, 20, town)
            response.write(xlsx_data)
            return response

        if 'pdf' in request.POST:
            response = HttpResponse(content_type='application/pdf')
            today = date.today()
            filename = 'pdf_demo' + today.strftime('%Y-%m-%d')
            response['Content-Disposition'] =\
                'attachement; filename={0}.pdf'.format(filename)
            buffer = BytesIO()
            report = PdfVentas(buffer, 'A4')
            pdf = report.report(compras, 'LIBRO DE VENTAS', total, mes)
            response.write(pdf)
            return response

    	context = {
	        'town': town,
	        'compras': ventas,
	    }

        return render(request, template_name, context)
        # except Exception, e:
        #     messages.error(request, 'No existen ventas')

    return render(request, template_name)


def ComprasAjax(request):

    if request.method == 'POST':
        fecha_de = request.POST['fecha_de']
        fecha_a = request.POST['fecha_a']
        grupo = request.POST['grupo']
        tipo_compra = request.POST['pago']

        datas = []
        vd = []
        totalfinal = 0

        if tipo_compra == '':
        	if grupo != '':
        		compracabezera = Compras.objects.filter(fecha__range=(fecha_de, fecha_a), grupo=grupo).order_by('fecha')
        	else:
        		compracabezera = Compras.objects.filter(fecha__range=(fecha_de, fecha_a)).order_by('fecha')
        else:
        	if grupo != '':
        		compracabezera = Compras.objects.filter(fecha__range=(fecha_de, fecha_a), grupo=grupo, tipodcompra=tipo_compra).order_by('fecha')
        	else:
        		compracabezera = Compras.objects.filter(fecha__range=(fecha_de, fecha_a), tipodcompra=tipo_compra).order_by('fecha')

        for cab in compracabezera:
        	det = DetalleCompra.objects.filter(compras=cab.pk)
        	for d in det:
        		total_compra = d.cantidad * d.pr_costo
        		totalfinal = totalfinal + total_compra
        		vd.append({
	            	'codigo': d.codigo,
	            	'descripcion': d.descripcion,
	            	'unidad': d.unidad,
	            	'cantidad': d.cantidad,
	            	'pr_costo': d.pr_costo,
	            	'total_compra': Decimal(total_compra.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)),
	            	'comprobantetxt': d.compras.comprobantetxt,
	            	'fecha': datetime.datetime.strptime(str(d.compras.fecha), '%Y-%m-%d').strftime("%d/%m/%Y"),
	            	'factura': d.compras.factura
	            })

        	vd.append({
            	'codigo': '',
            	'descripcion': 'Total Comp.',
            	'unidad': '',
            	'cantidad': '',
            	'pr_costo': '',
            	'total_compra': cab.total,
            	'comprobantetxt': '-------',
            	'fecha': '',
            	'factura': ''
            })
        print vd




        data_de = datetime.datetime.strptime(str(fecha_de), '%Y-%m-%d').strftime("%d/%m/%Y")
        data_a = datetime.datetime.strptime(str(fecha_a), '%Y-%m-%d').strftime("%d/%m/%Y")

        datas.append({
        	'data_de': data_de,
        	'data_a': data_a,
        	'total': Decimal(totalfinal.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)),
        	'detalle': vd
        })

        json_data = json.dumps(datas, cls=DjangoJSONEncoder)

        return HttpResponse(json_data, content_type='application/json')


def ReporteInventarios(request):

    template_name = "reportes/reporte_inventario.html"

    if request.method == 'POST':
        inventario = request.POST['inventario']
        imprimir = request.POST['imprimir']
        orden = request.POST['orden']
        grupo = request.POST['grupo']

        today = datetime.date.today()
        datas = []

        if imprimir == 'todo':
            if orden == 'codigo':
                if grupo != '':
                    item = Item.objects.filter(codigo__icontains=grupo).extra(select={'lower_name': 'lower(codigo)'}).order_by('lower_name')
                else:
                    item = Item.objects.all().extra(select={'lower_name': 'lower(codigo)'}).order_by('lower_name')
            else:
                if grupo != '':
                    item = Item.objects.filter(codigo__icontains=grupo).extra(select={'lower_name': 'lower(descripcion)'}).order_by('lower_name')
                else:
                    item = Item.objects.all().extra(select={'lower_name': 'lower(descripcion)'}).order_by('lower_name')
        else:
            if orden == 'codigo':
                if grupo != '':
                    item = Item.objects.filter(codigo__icontains=grupo).exclude(cantidad=0).extra(select={'lower_name': 'lower(codigo)'}).order_by('lower_name')
                else:
                    item = Item.objects.all().exclude(cantidad=0).extra(select={'lower_name': 'lower(codigo)'}).order_by('lower_name')
            else:
                if grupo != '':
                    item = Item.objects.filter(codigo__icontains=grupo).exclude(cantidad=0).extra(select={'lower_name': 'lower(descripcion)'}).order_by('lower_name')
                else:
                    item = Item.objects.all().exclude(cantidad=0).extra(select={'lower_name': 'lower(descripcion)'}).order_by('lower_name')

        it = []
        for i in item:
            print i.descripcion
            tc = i.cantidad*i.pr_costo
            it.append({
                'codigo': i.codigo,
                'descripcion': i.descripcion,
                'unidad': i.unidad,
                'cantidad': i.cantidad,
                'pr_costo': i.pr_costo,
                'total': Decimal(tc.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
            })

        datas.append({'inventario': inventario, 'fecha': today.strftime('%Y/%m/%d'),  'item': it})

        if 'excel' in request.POST:
            response = HttpResponse(content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=reporte_inventario.xlsx'
            xlsx_data = WriteToInventario(it, inventario, today.strftime('%Y/%m/%d'), 20, '')
            response.write(xlsx_data)
            return response

        if 'pdf' in request.POST:
            response = HttpResponse(content_type='application/pdf')
            today = date.today()
            filename = 'pdf_demo' + today.strftime('%Y-%m-%d')
            response['Content-Disposition'] =\
                'attachement; filename={0}.pdf'.format(filename)
            buffer = BytesIO()
            report = PdfVentas(buffer, 'A4')
            pdf = report.report(compras, 'LIBRO DE VENTAS', total, mes)
            response.write(pdf)
            return response

    	context = {
	        'town': town,
	        'compras': datas,
	    }

        return render(request, template_name, context)
    
    return render(request, template_name)


def InventariosAjax(request):
	if request.method == 'POST':
		inventario = request.POST['inventario']
		imprimir = request.POST['imprimir']
		orden = request.POST['orden']
		grupo = request.POST['grupo']

		today = datetime.date.today()
		datas = []
		# item = Item.objects.all()

		if imprimir == 'todo':
			if orden == 'codigo':
				if grupo != '':
					item = Item.objects.filter(codigo__icontains=grupo).extra(select={'lower_name': 'lower(codigo)'}).order_by('lower_name')
				else:
					item = Item.objects.all().extra(select={'lower_name': 'lower(codigo)'}).order_by('lower_name')
			else:
				if grupo != '':
					item = Item.objects.filter(codigo__icontains=grupo).extra(select={'lower_name': 'lower(descripcion)'}).order_by('lower_name')
				else:
					item = Item.objects.all().extra(select={'lower_name': 'lower(descripcion)'}).order_by('lower_name')
		else:
			if orden == 'codigo':
				if grupo != '':
					item = Item.objects.filter(codigo__icontains=grupo).exclude(cantidad=0).extra(select={'lower_name': 'lower(codigo)'}).order_by('lower_name')
				else:
					item = Item.objects.all().exclude(cantidad=0).extra(select={'lower_name': 'lower(codigo)'}).order_by('lower_name')
			else:
				if grupo != '':
					item = Item.objects.filter(codigo__icontains=grupo).exclude(cantidad=0).extra(select={'lower_name': 'lower(descripcion)'}).order_by('lower_name')
				else:
					item = Item.objects.all().exclude(cantidad=0).extra(select={'lower_name': 'lower(descripcion)'}).order_by('lower_name')

		it = []
		for i in item:
			print i.descripcion
			tc = i.cantidad*i.pr_costo
			it.append({
				'codigo': i.codigo,
				'descripcion': i.descripcion,
				'unidad': i.unidad,
				'cantidad': i.cantidad,
				'pr_costo': i.pr_costo,
				'total': Decimal(tc.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
			})

		datas.append({'inventario': inventario, 'fecha': today.strftime('%Y/%m/%d'),  'item': it})

		json_data = json.dumps(datas, cls=DjangoJSONEncoder)

		return HttpResponse(json_data, content_type='application/json')
# def buscarCompra(request):
#     idCompra = request.GET['id']
#     compra = Compras.objects.filter(comprobante=idCompra)
#     # print data
#     datas = []
#     for c in compra:
#         print c.fecha
#         detalle = DetalleCompra.objects.filter(compras=c)

#         vd = []
#         for d in detalle:
#             vd.append({
#                 "pk": d.pk,
#                 "pk_item": d.item.pk,
#                 "codigo": d.codigo,
#                 "unidad": d.unidad,
#                 "descripcion": d.descripcion,
#                 "cantidad": d.cantidad,
#                 "pr_costo": d.pr_costo
#             })
#         date_1 = datetime.datetime.strptime(str(c.fecha), '%Y-%m-%d').strftime("%d/%m/%Y")
#         datas.append({"fields": {
#             "comprobante": c.comprobante,
#             "factura": c.factura,
#             "fecha": date_1,
#             "tipodcompra": c.tipodcompra,
#             "tipodcompra2": c.tipodcompra2,
#             "grupo": c.grupo,
#             "proveedor": c.proveedor.nombre,
#             "proveedor_pk": c.proveedor.pk,
#             "proveedor_codigo": c.proveedor.codigo,
#             "detalle": vd,
#         }, "model": "compras.compras", "pk": c.pk})
#     json_data = json.dumps(datas, cls=DjangoJSONEncoder)
#     print 'esto es json'
#     print json_data

#     return HttpResponse(json_data, content_type='application/json')