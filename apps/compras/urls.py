from django.conf.urls import include, url
from .views import ListarCompras

# import debug_toolbar
urlpatterns = [

	url(r'^compras/$', 'apps.compras.views.compraCrear', name='compras'),
	url(r'^lista_compras/$', ListarCompras.as_view(), name='lista_compras'),


	url(r'^buscar_item/$', 'apps.compras.views.buscarProducto'),
	url(r'^buscar_compra/$', 'apps.compras.views.buscarCompra'),
	url(r'^buscar_proveedor/$', 'apps.compras.views.buscarProveedor'),
	url(r'^registrar_proveedor/$', 'apps.compras.views.addProveedor', name='registrar_proveedor'),
	url(r'^lista_proveedores/', 'apps.compras.views.listaProveedores', name="lista_proveedores"),
	url(r'^lista_items/', 'apps.compras.views.listaItems', name="lista_items"),
    url(r'^registrar_item/$', 'apps.compras.views.addItem', name='registrar_item'),
    url(r'^buscar_comprobante/$', 'apps.compras.views.buscarComprobante'),
    # url(r'^crearitem/$', 'apps.item.views.CrearItem', name='crearitem'),
    # url(r'^listar_item/', ListarItem.as_view(), name='listar_item'),
    url(r'^detalle_compra/(?P<pk>\d+)$', 'apps.compras.views.detalleCompra', name='detalle_compra'),
    # url(r'^edit_item/(?P<pk>\d+)$', EditItem.as_view(), name='edit_item'),
    # url(r'^delete_item/(?P<item>\d+)$', 'apps.item.views.DeleteItem', name='item_delete'),


]