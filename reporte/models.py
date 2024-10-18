from django.db import models

class reporte(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    Gravedad_eleccion= [
        (1,'Baja'),
        (2, 'Media'),
        (3,'Alta'),
    ]
    Urgencia_eleccion= [
        (1,'No urgente'),
        (2, 'Urgente'),
        (3,'Critica'),
    ]
    gravedad =models.IntegerField(choices=Gravedad_eleccion, default=1)
    urgencia =models.IntegerField(choices=Urgencia_eleccion, default=1)