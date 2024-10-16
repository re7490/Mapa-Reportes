from django.shortcuts import render, redirect, get_object_or_404
from .forms import reporteForm, Registroform
from .models import reporte
from django.contrib.auth import login
from django.contrib import messages



def home(request):
    return render(request, 'home.html')


def reportes(request):
    gravedad=request.GET.get('gravedad')
    urgencia=request.GET.get('urgencia')

    if gravedad:
        report= report.filter(gravedad=gravedad)
    if urgencia:
        report = report.filter(urgencia=urgencia)
    report = reporte.objects.all().order_by('-gravedad','-urgencia')
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
def mapa_piso3(request):
    return render(request,'mapa/piso3.html')
def mapa_piso4(request):
    return render(request,'mapa/piso4.html')
def mapa_piso0(request):
    return render(request,'mapa/piso-1.html')

def registrar(request):
    if request.method=='POST':
        form= Registroform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('postlogin')
    else:
        form=Registroform()
    return render(request,'registro.html',{'form':form})

def postlogin(request):
    return render(request, 'postlogin.html')