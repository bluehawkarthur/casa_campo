from django.conf.urls import include, url
from .views import ListarItem, DetalleItem
from .views import EditItem, DeleteItem


# import debug_toolbar
urlpatterns = [

    url(r'^crearitem/$', 'apps.item.views.CrearItem', name='crearitem'),
    url(r'^listar_item/', ListarItem.as_view(), name='listar_item'),
    url(r'^detalle_item/(?P<pk>\d+)$', DetalleItem.as_view(), name='detalle_item'),
    url(r'^edit_item/(?P<pk>\d+)$', EditItem.as_view(), name='edit_item'),
    url(r'^delete_item/(?P<item>\d+)$', 'apps.item.views.DeleteItem', name='item_delete'),

    # url(r'^edit_datosdosificacion/(?P<pk>\d+)$', EditDatosDosificacion.as_view(), name='edit_datosdosificacion'),
    # url(r'^delete_datosdosificacion/(?P<datosdosificacion>\d+)$', 'apps.config.views.DeleteDatosDosificacion', name='datosdosificacion_delete'),

]