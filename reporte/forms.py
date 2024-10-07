from django.forms import ModelForm
from .models import reporte

class reporteForm(ModelForm):
    class Meta:
        model = reporte
        fields = ['titulo','descripcion']