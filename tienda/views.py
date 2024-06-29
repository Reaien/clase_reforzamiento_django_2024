from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def home(request):
    productos = Producto.objects.all()
    data = {"productos" : productos}
    return render(request, 'tienda/index.html', data)

def agregar_producto(request):
    data = {'form': ProductoForm()}
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request, 'tienda/producto/agregar.html', data)

def listar_producto(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'tienda/producto/listar.html', data)

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {'form': ProductoForm(instance=producto)}
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Modificado Correctamente"
            return redirect(to="listar_producto")
        else:
            data["form"] = formulario
    return render(request, 'tienda/producto/modificar.html', data)

def eliminar_producto(id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_producto")