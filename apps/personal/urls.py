from django.conf.urls import include, url

from .views import ListarPersonal, EditPersonal, ListarAnticipo, BusquedaPersonal, EditAnticipo, BusquedaNombre


urlpatterns = [

    # PERSONAL
    url(r'^crear_personal/$', 'apps.personal.views.crearPersonal', name='crear_personal'),
    url(r'^listar_personal/$', ListarPersonal.as_view(), name='listar_personal'),
    url(r'^edit_personal/(?P<pk>\d+)$', EditPersonal.as_view(), name='edit_personal'),
    url(r'^delete_personal/(?P<id>\d+)$', 'apps.personal.views.deletePersonal', name='personal_delete'),

    # ANTICIPOS
    url(r'^crear_anticipo/$', 'apps.personal.views.crearAnticipo', name='crear_anticipo'),
    url(r'^listar_anticipos/$', ListarAnticipo.as_view(), name='listar_anticipos'),
    url(r'^edit_anticipo/(?P<pk>\d+)$', EditAnticipo.as_view(), name='edit_anticipo'),
    url(r'^delete_anticipo/(?P<id>\d+)$', 'apps.personal.views.deleteAnticipo', name='anticipo_delete'),

    url(r'^busqueda_personal/$', BusquedaPersonal.as_view(), name='busqueda_personal'),
    url(r'^busqueda_nombre/$', BusquedaNombre.as_view(), name='busqueda_nombre'),

]

