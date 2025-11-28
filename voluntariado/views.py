from django.shortcuts import render, redirect, get_object_or_404
from .models import Voluntario, Evento
from .forms import VoluntarioForm, EventoForm

def index(request):
    return render(request, 'index.html')

def lista_voluntarios(request):
    voluntarios = Voluntario.objects.all()
    return render(request, 'lista_voluntarios.html', {'voluntarios': voluntarios})

def detalle_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    return render(request, 'detalle_voluntario.html', {'voluntario': voluntario})

def crear_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_voluntarios')
    else:
        form = VoluntarioForm()
    return render(request, 'crear_voluntario.html', {'form': form})

def editar_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, instance=voluntario)
        if form.is_valid():
            form.save()
            return redirect('lista_voluntarios')
    else:
        form = VoluntarioForm(instance=voluntario)
    return render(request, 'editar_voluntario.html', {'form': form})

def eliminar_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    if request.method == 'POST':
        voluntario.delete()
        return redirect('lista_voluntarios')
    return render(request, 'eliminar_voluntario.html', {'voluntario': voluntario})

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def detalle_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'detalle_evento.html', {'evento': evento})

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'crear_evento.html', {'form': form})

def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'editar_evento.html', {'form': form})

def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('lista_eventos')
    return render(request, 'eliminar_evento.html', {'evento': evento})