from django.db import models

class reporte(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    pin_location = models.CharField(max_length=50, null=True, blank=True)  # Campo para almacenar la ubicación del pin
    completado = models.BooleanField(default=False)
    fecha_completado=models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.titulo
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
    x= models.IntegerField()
    y= models.IntegerField()
    piso=models.IntegerField(default=-1)