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
        producto_forms = [CarritoProductoForm(request.POST, prefix=str(i)) for i in range(len(request.POST.getlist('producto')))]  # Generamos un formulario para cada producto

        if carrito_form.is_valid() and all(form.is_valid() for form in producto_forms):
            # Guardamos el carrito
            carrito = carrito_form.save()

            # Guardamos los productos en el carrito
            for form in producto_forms:
                carrito_producto = form.save(commit=False)
                carrito_producto.carrito = carrito
                carrito_producto.save()

            return redirect('comercio')  # Redirige a la página principal después de guardar
    else:
        carrito_form = CarritoForm()
        producto_forms = [CarritoProductoForm(prefix=str(i)) for i in range(5)]  # Creando 5 formularios como ejemplo

    return render(request, 'comercio/crear_carrito.html', {
        'carrito_form': carrito_form,
        'producto_forms': producto_forms,
        'productos': Producto.objects.all(),  # Para mostrar la lista de productos disponibles
    })

# Vista para listar todos los clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()  # Trae todos los clientes
    return render(request, 'comercio/lista_clientes.html', {'clientes': clientes})

# Vista para listar todos los productos
def lista_productos(request):
    productos = Producto.objects.all()  # Trae todos los productos
    return render(request, 'comercio/lista_productos.html', {'productos': productos})

# Vista para listar todos los carritos
def lista_carritos(request):
    carritos = Carrito.objects.all()  # Trae todos los carritos
    return render(request, 'comercio/lista_carritos.html', {'carritos': carritos})

