from django.db import models

class Voluntario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField()
    voluntarios = models.ManyToManyField(Voluntario, related_name="eventos")

    def __str__(self):
        return self.titulo

# --- PARA LA GALERÍA ---
class FotoEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='fotos')
    imagen = models.ImageField(upload_to='eventos_galeria/')
    
    def __str__(self):
        return f"Foto de {self.evento.titulo}"