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
    class Meta:
        model=User
        fields=['username','password1','password2']
    def save(self,commit=True):
        user= super(Registroform,self).save(commit=False)
        if commit:
            user.save()
        return user