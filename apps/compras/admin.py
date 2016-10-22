from django.contrib import admin
from .models import Compras, DetalleCompra, ComprasHistory, DetalleCompraHystory

# Register your models here.
admin.site.register(Compras)
admin.site.register(DetalleCompra)
admin.site.register(ComprasHistory)
admin.site.register(DetalleCompraHystory)
