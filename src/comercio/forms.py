from django import forms

from .models import Cliente, Producto, Carrito, CarritoProducto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class CarritoForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = ['cliente']

class CarritoProductoForm(forms.ModelForm):
    class Meta:
        model = CarritoProducto
        fields = ['producto', 'cantidad']
