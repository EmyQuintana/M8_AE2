# voluntariado/models.py
from django.db import models

class Voluntario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")
    # --- NUEVO CAMPO PARA PONERLE FOTO DE IDENTIFICACION A CADA VOLUNTARIO 
    foto = models.ImageField(upload_to='perfiles_voluntarios/', blank=True, null=True, verbose_name="Foto de Perfil")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = "Voluntario"
        verbose_name_plural = "Voluntarios"

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título del Evento")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha = models.DateField(verbose_name="Fecha del Evento")
    # related_name='eventos' permite acceder desde Voluntario así: voluntario.eventos.all()
    voluntarios = models.ManyToManyField(Voluntario, related_name="eventos", blank=True)

    class Meta:
        ordering = ['fecha']  # Ordenar por fecha, del más próximo al más lejano
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.titulo

class FotoEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='fotos')
    imagen = models.ImageField(upload_to='eventos_galeria/')
    
    def __str__(self):
        return f"Foto de {self.evento.titulo}"