from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

def index(request):
    productos = Producto.objects.all()
    return render(request, 'app_producto/index.html', {'productos': productos})

def add_producto(request):
    success = False
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = ProductoForm()
    return render(request, 'app_producto/add.html', {'form': form, 'success': success})

def edit_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    success = False
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'app_producto/edit.html', {'form': form, 'success': success})

def delete_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('index')
    return render(request, 'app_producto/delete.html', {'producto': producto})
