from django.shortcuts import render, redirect
from .forms import ClienteForm, ProductoForm, CarritoForm, CarritoProductoForm
from .models import Cliente, Producto, Carrito, CarritoProducto

def index(request):
    return render(request, "comercio/index.html")

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_cliente')
    else:
        form = ClienteForm()
    return render(request, 'comercio/crear_cliente.html', {'form': form})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_producto')
    else:
        form = ProductoForm()
    return render(request, 'comercio/crear_producto.html', {'form': form})

def crear_carrito(request):
    if request.method == 'POST':
        carrito_form = CarritoForm(request.POST)

        productos_ids = request.POST.getlist('producto')
        cantidades = request.POST.getlist('cantidad')

        producto_forms = []
        for i in range(len(productos_ids)):
            data = {
                'producto': productos_ids[i],
                'cantidad': cantidades[i]
            }
            form = CarritoProductoForm(data, prefix=str(i))
            producto_forms.append(form)

        if carrito_form.is_valid() and all([form.is_valid() for form in producto_forms]):
            carrito = carrito_form.save()

            for form in producto_forms:
                producto = form.cleaned_data['producto']
                cantidad = form.cleaned_data['cantidad']

                if producto.stock >= cantidad:
                    CarritoProducto.objects.create(carrito=carrito, producto=producto, cantidad=cantidad)
                    producto.stock -= cantidad
                    producto.save()
                else:
                    return render(request, 'comercio/crear_carrito.html', {
                        'carrito_form': carrito_form,
                        'producto_forms': producto_forms,
                        'error': f"No hay suficiente stock para {producto.nombre}."
                    })
                
            return redirect('lista_carritos')
    else:
        carrito_form = CarritoForm()
        producto_forms = [CarritoProductoForm(prefix=str(i)) for i in range(2)]

    return render(request, 'comercio/crear_carrito.html', {
        'carrito_form': carrito_form,
        'producto_forms': producto_forms,
    })

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'comercio/lista_clientes.html', {'clientes': clientes})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'comercio/lista_productos.html', {'productos': productos})

def lista_carritos(request):
    carritos = Carrito.objects.prefetch_related('productos')
    context = {
        'carritos': carritos,
    }
    return render(request, 'comercio/lista_carritos.html', context)