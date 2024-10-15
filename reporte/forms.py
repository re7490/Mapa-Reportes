from django.forms import ModelForm
from django import forms
from .models import reporte

class reporteForm(ModelForm):
    class Meta:
        model = reporte
        fields = ['titulo','descripcion','gravedad','urgencia']
        widgets = {
            'gravedad': forms.Select(choices=reporte.Gravedad_eleccion),
            'urgencia': forms.Select(choices=reporte.Urgencia_eleccion),
        }