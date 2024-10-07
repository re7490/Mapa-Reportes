from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import reporteForm
from .models import reporte

def home(request):
    return render(request, 'home.html')

def signup(request):
    
    if request.method =='GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(username=request.POST['username'], password=request.POST['password2'])
                usuario.save()
                return HttpResponse('Usuario creado :)')
            except:
                return HttpResponse('El usuario ya existe')
        return HttpResponse('contraseña no coincide')

def reportes(request):
    report = reporte.objects.all()
    return render(request, 'reportes.html', {'r': report})

def crear_reporte(request):

    if request.method == 'GET':
        return render(request, 'crear_reporte.html', {
            'form': reporteForm})
    else:
        reporte = reporteForm(request.POST)
        reporte.save()
        return redirect('reportes')