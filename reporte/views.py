from django.shortcuts import render, redirect, get_object_or_404
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

def reporte_(request, id):
    if request.method == 'GET':
        re = get_object_or_404(reporte, pk=id)
        form = reporteForm(instance=re)
        return render(request, 'reporte_.html', {'r': re, 'form': form})
    else:
        re = get_object_or_404(reporte, pk=id)
        form = reporteForm(request.POST, instance=re)
        form.save()
        return redirect('reportes')

def borrar_reporte(request, id):
    re = get_object_or_404(reporte, pk=id)
    if request.method == "POST":
        re.delete()
        return redirect('reportes')

def mapa_piso1(request):
    return render(request,'mapa/piso1.html')
def mapa_piso2(request):
    return render(request,'mapa/piso2.html')
def mapa_piso4(request):
    return render(request,'mapa/piso4.html')
def mapa_piso0(request):
    return render(request,'mapa/piso-1.html')