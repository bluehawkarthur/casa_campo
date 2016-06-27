# views.py
from django.shortcuts import render_to_response as render, redirect
from django.template import RequestContext as ctx
from django.forms.models import inlineformset_factory
from django.views.generic import TemplateView
from .models import Compras, DetalleCompra
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from django.core import serializers
import json
from django.db import transaction
from django.contrib import messages
from apps.item.models import Item
from apps.proveedor.models import Proveedor
import decimal
# from apps.reportes.htmltopdf import render_to_pdf
from datetime import date
import datetime


def buscarProducto(request):
    idProducto = request.GET['id']
    descripcion = Item.objects.filter(codigo__icontains=idProducto)
    data = serializers.serialize('json', descripcion, fields=('pk', 'codigo', 'unidad', 'descripcion', 'cantidad', 'pr_costo'))

    return HttpResponse(data, content_type='application/json')


def buscarProveedor(request):
    idProveedor = request.GET['id']
    descripcion = Proveedor.objects.filter(razon_social__icontains=idProveedor, empresa=request.user.empresa)
    if descripcion:
        data = serializers.serialize(
        'json', descripcion, fields=('pk', 'nit', 'razon_social'))
    else:
        nit = Proveedor.objects.filter(nit__contains=idProveedor, empresa=request.user.empresa)
        data = serializers.serialize(
            'json', nit, fields=('pk', 'nit', 'razon_social'))
    return HttpResponse(data, content_type='application/json')


def compraCrear(request):

    form = None
    if request.method == 'POST':
    	
        sid = transaction.savepoint()
        # try:
        print 'comprassssssss'
        print request.body
        proceso = json.loads(request.body)
        
        print proceso
        if len(proceso['producto']) <= 0:
            msg = 'No se ha seleccionado ningun producto'
            raise Exception(msg)

        total = 0
        # calculo total de compras
        for k in proceso['producto']:
            total += decimal.Decimal(k['subtotal'])

        date_1 = datetime.datetime.strptime(proceso['fecha'], '%d/%m/%Y').strftime("%Y-%m-%d")


        print total
        crearCompra = Compras(
            comprobante=proceso['comprobante'],
            factura=proceso['factura'],
            fecha=date_1,
            tipodcompra=proceso['tipodcompra'],
            total=total,
        )
        crearCompra.save()

        for k in proceso['producto']:
            print '====== los productos son ======'
            print k['descripcion']
            print '==============================='

            item = Item.objects.filter(id=k['pk'])
            cantidad_total = item[0].cantidad + int(k['cantidad'])
            item.update(cantidad=cantidad_total)

            crearDetalle = DetalleCompra(
                compras=crearCompra,
                codigo=k['codigo_item'],
                unidad=k['unidad'],
                descripcion=k['descripcion'],
                cantidad=int(k['cantidad']),
                pr_costo=decimal.Decimal(k['pr_costo']),
                item=Item.objects.get(id=k['pk']),
            )
            crearDetalle.save()


            # return HttpResponseRedirect(reverse('detallecompra', args=(crearCompra.pk,)))
            # return render('compras/compra.html', {'form': form,  'popup': True, 'pk': crearCompra.pk, 'url': '/detalle_compra/' }, context_instance=ctx(request))
        # return render('compras/compra.html', {'form': form}, context_instance=ctx(request))
        return HttpResponse(json.dumps(request.body), content_type='application/json')
        # except Exception, e:
        #     try:
        #         transaction.savepoint_rollback(sid)
        #     except:
        #         pass
        #     messages.error(request, e)

    return render('compras/compra.html', {'form': form}, context_instance=ctx(request))


# def detalleCompra(request, pk):
#     print pk
#     compra = Compra.objects.filter(id=pk)
#     detalle = DetalleCompra.objects.filter(compra=compra)


#     vd = []
#     for d in detalle:
#         vd.append(d)

#     print vd

#     data = {
#         'nit': compra[0].nit,
#         'razon_social': compra[0].razon_social,
#         'nro_factura': compra[0].nro_factura,
#         'nro_autorizacion': compra[0].nro_autorizacion,
#         'fecha': compra[0].fecha,
#         'cod_control': compra[0].cod_control,
#         'tipo_compra': compra[0].tipo_compra,
#         'cantidad_dias': compra[0].cantidad_dias,
#         'total': compra[0].total,
#         'detalle': vd
        
#     }

#     print compra
#     return render('compras/detalle.html', data, context_instance=ctx(request))


def detalleCompra(request, pk):
    print pk
    compra = Compra.objects.filter(id=pk)
    detalle = DetalleCompra.objects.filter(compra=compra)

    vd = []
    for d in detalle:
        vd.append(d)

    print vd

    data = {
        'nit': compra[0].nit,
        'razon_social': compra[0].razon_social,
        'nro_factura': compra[0].nro_factura,
        'nro_autorizacion': compra[0].nro_autorizacion,
        'fecha': compra[0].fecha,
        'cod_control': compra[0].cod_control,
        'tipo_compra': compra[0].tipo_compra,
        'cantidad_dias': compra[0].cantidad_dias,
        'total': compra[0].total,
        'detalle': vd,
        'empresa': request.user.get_empresa(),
        'dias': compra[0].cantidad_dias,
        'nro_nota': compra[0].nro_nota,
        'user': request.user,

    }
    messages.success(request, 'La compra se ha realizado satisfactoriamente')
    print compra
    return render_to_pdf('reportes/rep_detallecompra.html', data)
