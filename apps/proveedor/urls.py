from django.conf.urls import include, url
from .views import ListarProvedor, DetalleProveedor
from .views import EditProveedor, DeleteProveedor


# import debug_toolbar
urlpatterns = [
    url(r'^crear_proveed/$', 'apps.proveedor.views.CrearProveedor', name='crear_proveed'),
    url(r'^listar_proveed/', ListarProvedor.as_view(), name='listar_proveed'),
    url(r'^detalle_proveed/(?P<pk>\d+)$', DetalleProveedor.as_view(), name='detalle_proveed'),
    url(r'^edit_prove/(?P<pk>\d+)$', EditProveedor.as_view(), name='edit_prove'),
    url(r'^delete_proveedor/(?P<proveedor>\d+)$', 'apps.proveedor.views.DeleteProveedor', name='proveedor_delete'),
    # url(r'^edit_datosdosificacion/(?P<pk>\d+)$', EditDatosDosificacion.as_view(), name='edit_datosdosificacion'),
    # url(r'^delete_datosdosificacion/(?P<datosdosificacion>\d+)$', 'apps.config.views.DeleteDatosDosificacion', name='datosdosificacion_delete'),

]