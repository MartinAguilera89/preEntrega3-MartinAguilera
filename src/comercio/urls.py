from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="comercio"),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('carritos/', views.lista_carritos, name='lista_carritos'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('crear_carrito/', views.crear_carrito, name='crear_carrito'),
]