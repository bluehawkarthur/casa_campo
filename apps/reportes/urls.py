from django.conf.urls import include, url
from .views import ListarKardexAlmacen, EditKardexAlmacen

urlpatterns = [

	# url(r'^compras/$', 'apps.compras.views.compraCrear', name='compras'),
	url(r'^lista_kalm/$', ListarKardexAlmacen.as_view(), name='lista_kalm'),
    url(r'^edit_kalm/(?P<pk>\d+)$', EditKardexAlmacen.as_view(), name='edit_kalm'),
    url(r'^delete_kalm/(?P<kar>\d+)$', 'apps.reportes.views.DeleteKalm', name='kalm_delete'),
    url(r'^reporte_compras/$', 'apps.reportes.views.ReporteCompras', name='reporte_compras'),
    url(r'^compras_ajax/$', 'apps.reportes.views.ComprasAjax', name='compras_ajax'),
    url(r'^inventarios/$', 'apps.reportes.views.ReporteInventarios', name='inventarios'),
    url(r'^inventario_ajax/$', 'apps.reportes.views.InventariosAjax', name='inventario_ajax'),
    url(r'^lista_provedores/$', 'apps.reportes.views.listaProveedores', name='lista_provedores'),
    url(r'^pagos_provedores/$', 'apps.reportes.views.PagosProveedores', name='pagos_provedores'),

	# url(r'^buscar_item/$', 'apps.compras.views.buscarProducto'),
	# url(r'^buscar_compra/$', 'apps.compras.views.buscarCompra'),
	# url(r'^buscar_proveedor/$', 'apps.compras.views.buscarProveedor'),
	# url(r'^registrar_proveedor/$', 'apps.compras.views.addProveedor', name='registrar_proveedor'),
	# url(r'^lista_proveedores/', 'apps.compras.views.listaProveedores', name="lista_proveedores"),
	# url(r'^lista_items/', 'apps.compras.views.listaItems', name="lista_items"),
 #    url(r'^registrar_item/$', 'apps.compras.views.addItem', name='registrar_item'),
    # url(r'^crearitem/$', 'apps.item.views.CrearItem', name='crearitem'),
    # url(r'^listar_item/', ListarItem.as_view(), name='listar_item'),
    # url(r'^detalle_item/(?P<pk>\d+)$', DetalleItem.as_view(), name='detalle_item'),


]