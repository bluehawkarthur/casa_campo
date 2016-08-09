from django.conf.urls import include, url

# import debug_toolbar
urlpatterns = [

	url(r'^compras/$', 'apps.compras.views.compraCrear', name='compras'),
	url(r'^buscar_item/$', 'apps.compras.views.buscarProducto'),
	url(r'^buscar_compra/$', 'apps.compras.views.buscarCompra'),
	url(r'^buscar_proveedor/$', 'apps.compras.views.buscarProveedor'),
	url(r'^registrar_proveedor/$', 'apps.compras.views.addProveedor', name='registrar_proveedor'),
	url(r'^lista_proveedores/', 'apps.compras.views.listaPrueba', name="lista_proveedores"),
    url(r'^registrar_item/$', 'apps.compras.views.addItem', name='registrar_item'),
    # url(r'^crearitem/$', 'apps.item.views.CrearItem', name='crearitem'),
    # url(r'^listar_item/', ListarItem.as_view(), name='listar_item'),
    # url(r'^detalle_item/(?P<pk>\d+)$', DetalleItem.as_view(), name='detalle_item'),
    # url(r'^edit_item/(?P<pk>\d+)$', EditItem.as_view(), name='edit_item'),
    # url(r'^delete_item/(?P<item>\d+)$', 'apps.item.views.DeleteItem', name='item_delete'),


]