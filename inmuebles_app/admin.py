from django.contrib import admin
from .models import Comuna, Inmueble, Region, Perfil
# Register your models here.

class RegionAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('id', 'direccion', 'tipo_inmueble', 'valor_arriendo', 'disponible', 'comuna')
    list_filter = ('disponible', 'tipo_inmueble', 'comuna')
    search_fields = ('direccion', 'descripcion')

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'tipo_usuario', 'rut', 'telefono')
    list_filter = ('tipo_usuario',)

admin.site.register(Region, RegionAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Inmueble, InmuebleAdmin)
admin.site.register(Perfil, PerfilAdmin)
