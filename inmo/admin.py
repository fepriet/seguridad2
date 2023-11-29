from django.contrib import admin
from .models import *


# Register your models here.

class PropiedadAdmin(admin.ModelAdmin):
     list_display=('propiedad_id','comuna', 'direccion','num_dor','num_banios','num_estac','precio','tipo_negocio','disponible','owner','tipoContrato')
admin.site.register(Propiedad, PropiedadAdmin)

class TipoPropiedadAdmin(admin.ModelAdmin):
     list_display=('idTipo','nombreTipo')
admin.site.register(TipoPropiedad, TipoPropiedadAdmin)

class ContratoPropiedadAdmin(admin.ModelAdmin):
     list_display=('idContrato','nombreContrato')
admin.site.register(ContratoPropiedad, ContratoPropiedadAdmin)

class ComunaPropiedadAdmin(admin.ModelAdmin):
     list_display=('idComuna','nombreComuna')
admin.site.register(ComunaPropiedad, ComunaPropiedadAdmin)

class CompraAdmin(admin.ModelAdmin):
     list_display=('compra_id','propiedad_id','cliente','numero','fecha','tipo_pago','comentario','contactado')
admin.site.register(Compra, CompraAdmin)
