from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Libro
from .forms import LibroForm

def menu(request):
    return render(request, 'biblioteca/menu.html')

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/listar_libros.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Libro guardado exitosamente!')
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/crear_libro.html', {'form': form})
def modificar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'biblioteca/modificar_libro.html', {'form': form, 'libro': libro})

def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'biblioteca/eliminar_libro.html', {'libro': libro})
