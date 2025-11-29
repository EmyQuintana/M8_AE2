from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # Para feedback al usuario
from django.db import transaction, IntegrityError # Para seguridad en base de datos
from .forms import VoluntarioForm, EventoForm
from .models import Voluntario, Evento, FotoEvento
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    return render(request, 'index.html')

# CRUD DE VOLUNTARIOS

def lista_voluntarios(request):
    # Ordenamos por id descendente (o fecha) como en el ejemplo de bicicletas (visto en clases)
    voluntarios = Voluntario.objects.all().order_by('-id')
    return render(request, 'lista_voluntarios.html', {'voluntarios': voluntarios})

def detalle_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    return render(request, 'detalle_voluntario.html', {'voluntario': voluntario})

@permission_required('voluntariado.add_voluntario') # Solo usuarios con permiso de "Agregar"
def crear_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # transaction.atomic asegura que si algo falla, no se guarde nada a medias
                with transaction.atomic():
                    form.save()
                messages.success(request, "Voluntario registrado correctamente.")
                return redirect('lista_voluntarios')
            except IntegrityError:
                messages.error(request, "Ocurrió un error al guardar el voluntario.")
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = VoluntarioForm()
    return render(request, 'crear_voluntario.html', {'form': form})

@permission_required('voluntariado.change_voluntario') # Solo usuarios con permiso de "Cambiar/Editar"
def editar_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, request.FILES, instance=voluntario)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                messages.success(request, "Datos del voluntario actualizados.")
                return redirect('lista_voluntarios')
            except IntegrityError:
                messages.error(request, "Error al actualizar los datos.")
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = VoluntarioForm(instance=voluntario)
    return render(request, 'editar_voluntario.html', {'form': form, 'voluntario': voluntario})

@permission_required('voluntariado.delete_voluntario') # Solo Admin
def eliminar_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    if request.method == 'POST':
        try:
            voluntario.delete()
            messages.success(request, "Voluntario eliminado exitosamente.")
            return redirect('lista_voluntarios')
        except IntegrityError:
            # Útil si el voluntario está vinculado a algo que impide borrarlo
            messages.error(request, "No se puede eliminar este voluntario porque tiene registros asociados.")
    return render(request, 'eliminar_voluntario.html', {'voluntario': voluntario})

# CRUD DE EVENTOS

def lista_eventos(request):
    eventos = Evento.objects.all().order_by('-fecha') # Ordenamos por fecha
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def detalle_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'detalle_evento.html', {'evento': evento})

@permission_required('voluntariado.add_evento') # Solo quien pueda agregar
def crear_evento(request):
    if request.method == 'POST':
        # AGREGAR request.FILES
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    evento = form.save()
                    # Lógica para guardar la foto extra
                    foto = form.cleaned_data.get('foto_portada')
                    if foto:
                        FotoEvento.objects.create(evento=evento, imagen=foto)
                return redirect('lista_eventos')
            except Exception as e:
                pass # Manejo de error simple
    else:
        form = EventoForm()
    return render(request, 'crear_evento.html', {'form': form})

@permission_required('voluntariado.change_evento') # Admin y Gestor
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        # AGREGAR request.FILES AQUÍ TAMBIÉN
        form = EventoForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            try:
                with transaction.atomic():
                    evento = form.save()
                    # Lógica para guardar la foto extra
                    foto = form.cleaned_data.get('foto_portada')
                    if foto:
                        FotoEvento.objects.create(evento=evento, imagen=foto)
                return redirect('lista_eventos')
            except Exception as e:
                pass
    else:
        form = EventoForm(instance=evento)
    return render(request, 'editar_evento.html', {'form': form, 'evento': evento})

@permission_required('voluntariado.delete_evento') # Solo Admin
def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, "Evento eliminado.")
        return redirect('lista_eventos')
    return render(request, 'eliminar_evento.html', {'evento': evento})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada exitosamente. ¡Ahora puedes iniciar sesión!")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})