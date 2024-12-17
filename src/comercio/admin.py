from django.contrib import admin

from .models import Cliente, Producto, Carrito, CarritoProducto

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha_creacion', 'productos_relacionados')
    
    def productos_relacionados(self, obj):
        return ", ".join(
            [f"{relacion.producto.nombre} (x{relacion.cantidad})" for relacion in obj.carritoproducto_set.all()]
        )
    productos_relacionados.short_description = "Productos"

