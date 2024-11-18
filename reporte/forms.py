from django.forms import ModelForm
from django import forms
from .models import reporte
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class reporteForm(ModelForm):
    class Meta:
        model = reporte
        fields = ['titulo','descripcion','gravedad','urgencia']
        widgets = {
            'gravedad': forms.Select(choices=reporte.Gravedad_eleccion),
            'urgencia': forms.Select(choices=reporte.Urgencia_eleccion),
        }

class Registroform(UserCreationForm):
    llave = forms.CharField(max_length=100, required=True, help_text="Ingresa la llave de empleado")
    class Meta:
        model=User
        fields=['username','password1','password2','llave']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'espacio':'nombre usuario'})
        self.fields['username'].label = "Nombre de usuario"
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        
    def clean_llave(self):
        llave = self.cleaned_data.get('llave')
        if llave != 'clave-empleado':
            raise forms.ValidationError('La llave proporcionada no es válida.')
        return llave
