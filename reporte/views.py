from django.shortcuts import render, redirect, get_object_or_404 
from .forms import reporteForm, Registroform
from .models import reporte
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from django.utils import timezone
from django.utils.timezone import now

def home(request):
    reportes= reporte.objects.filter(completado=False)
    return render(request, 'home.html',{'reportes':reportes})

def reportes(request):
    gravedad = request.GET.get('gravedad')
    urgencia = request.GET.get('urgencia')

    report = reporte.objects.all().order_by('-gravedad','-urgencia')  # Corregido el uso de report
    if gravedad:
        report = report.filter(gravedad=gravedad)
    if urgencia:
        report = report.filter(urgencia=urgencia)

    return render(request, 'reportes.html', {'r': report})

def crear_reporte(request):
    if request.method == 'GET':
        return render(request, 'crear_reporte.html', {
            'form': reporteForm
        })
    else:
        reporte_form = reporteForm(request.POST)
        if reporte_form.is_valid():
            nuevo_reporte = reporte_form.save(commit=False)  # No guardes aún en la base de datos

            # Captura la ubicación del pin
            pin_location = request.POST.get('pin_location')
            nuevo_reporte.pin_location = pin_location  # Asigna la ubicación del pin al reporte
            
            nuevo_reporte.x=float(request.POST.get('x'))
            nuevo_reporte.y=float(request.POST.get('y'))
            piso=request.POST.get('piso',-1)
            nuevo_reporte.piso=int(piso)

            nuevo_reporte.save()  # Guarda el reporte en la base de datos
            if request.user.is_authenticated: # Verifica si un usuario esta iniciado
                request.session['nuevo_reporte']=True
                return redirect('postlogin')  # Manda notificacion a los usuarios/empleados
            return redirect('home')

def reporte_(request, id):
    if request.method == 'GET':
        re = get_object_or_404(reporte, pk=id)
        form = reporteForm(instance=re)
        reportes= reporte.objects.filter(completado=False)
        return render(request, 'reporte_.html', {'r': re, 'form': form,'reportes':reportes})
    else:
        re = get_object_or_404(reporte, pk=id)
        form = reporteForm(request.POST, instance=re)
        form.save()
        return redirect('home')

#SOLO usuarios podran brorrar o completar el reporte
@login_required
def completar_reporte(request, id):
    re = get_object_or_404(reporte, pk=id)
    if request.method == "POST":
        re.completado = True
        re.fecha_completado = now()
        re.save()
        return redirect('postlogin')

@login_required
def borrar_reporte(request, id):
    re = get_object_or_404(reporte, pk=id)
    if request.method == "POST":
        re.delete()
        return redirect('postlogin')

def mapa_piso0(request): #piso -1
    reportes= reporte.objects.filter(completado=False, piso=-1)
    reportes_data = [{
        'titulo': reporte.titulo,
        'descripcion': reporte.descripcion,
        'x': reporte.x,
        'y': reporte.y
    } for reporte in reportes]
    context= {"reportes":json.dumps(reportes_data)}
    return render(request, 'mapa/piso-1.html',context)

def mapa_piso1(request):
    reportes= reporte.objects.filter(completado=False, piso=1)
    reportes_data = [{
        'titulo': reporte.titulo,
        'descripcion': reporte.descripcion,
        'x': reporte.x,
        'y': reporte.y
    } for reporte in reportes]
    context= {"reportes":json.dumps(reportes_data)}
    return render(request, 'mapa/piso1.html',context)

def mapa_piso2(request):
    reportes= reporte.objects.filter(completado=False, piso=2)
    reportes_data = [{
        'titulo': reporte.titulo,
        'descripcion': reporte.descripcion,
        'x': reporte.x,
        'y': reporte.y
    } for reporte in reportes]
    context= {"reportes":json.dumps(reportes_data)}
    return render(request, 'mapa/piso2.html',context)

def seleccionar_piso(request):
    reportes= reporte.objects.filter(completado=False)
    if not reportes:
        messages.info(request, "No hay reportes.")
    if request.method=='POST':
        piso=request.POST.get('piso')
        return redirect(f'/piso{piso}')
    return render(request,'seleccionar_piso.html',{'reportes':reportes})

#SISTEMA DE CUENTAS
def registrar(request):
    if request.method == 'POST':
        form = Registroform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postlogin')
    else:
        form = Registroform()
    return render(request, 'registro.html', {'form': form})

#Vista/"home" de usuario
@login_required
def postlogin(request):
    usuario=request.user
    ultima_conexion=request.user.last_login or timezone.now()
    reportes_nuevos=reporte.objects.filter(fecha__gt=ultima_conexion).count()
    reportes_completados=reporte.objects.filter(completado=True,fecha_completado__gt=ultima_conexion).count()
    nuevo_reporte=request.session.pop('nuevo_reporte',False) # Ve si hay nuevo reporte
    reportes = reporte.objects.filter(completado=False).order_by('-id') #para mostrar lista de reportes
    context={'usuario':usuario,'reportes_nuevos':reportes_nuevos,'reportes_completados':reportes_completados,'r':reportes,'nuevo_reporte':nuevo_reporte}
    return render(request, 'postlogin.html', context)

@login_required
def lista_reportes_completados(request):
    piso = request.GET.get('piso', None)
    urgencia = request.GET.get('urgencia', None)
    gravedad = request.GET.get('gravedad', None)
    reportes_completados = reporte.objects.filter(completado=True)
    if piso:
        reportes_completados = reportes_completados.filter(piso=piso)
    if urgencia:
        reportes_completados = reportes_completados.filter(urgencia=urgencia)
    if gravedad:
        reportes_completados = reportes_completados.filter(gravedad=gravedad)
    reportes_completados = reportes_completados.order_by('-fecha_completado')
    return render(request, 'reportes_completados.html', {'reportes': reportes_completados,'piso': piso,'urgencia': urgencia,'gravedad': gravedad,})