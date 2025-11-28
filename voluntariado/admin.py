from django.contrib import admin
# Importamos también el nuevo modelo FotoEvento
from .models import Voluntario, Evento, FotoEvento

# Configuración para que las fotos aparezcan DENTRO del Evento
class FotoEventoInline(admin.TabularInline):
    model = FotoEvento
    extra = 1  # Muestra 1 espacio vacío listo para subir foto

class EventoAdmin(admin.ModelAdmin):
    # Aquí conectamos el inline al admin del evento
    inlines = [FotoEventoInline]
    list_display = ('titulo', 'fecha') # Opcional: mejora la lista

# Registramos los modelos
admin.site.register(Voluntario)
# IMPORTANTE: Registramos Evento usando nuestra configuración especial EventoAdmin
admin.site.register(Evento, EventoAdmin)