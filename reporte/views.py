from django.shortcuts import render, redirect, get_object_or_404 
from .forms import reporteForm, Registroform
from .models import reporte
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

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
            
            nuevo_reporte.save()  # Guarda el reporte en la base de datos
            messages.success(request, "Reporte enviado :)")
            if request.user.is_authenticated: # Verifica si un usuario esta iniciado
                request.session['nuevo_reporte']=True
                return redirect('postlogin')  # Manda notificacion a los usuarios/empleados
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

def completar_reporte(request, id):
    re = get_object_or_404(reporte, pk=id)
    if request.method == "POST":
        re.completado = True
        re.save()
        return redirect('reportes')

def borrar_reporte(request, id):
    re = get_object_or_404(reporte, pk=id)
    if request.method == "POST":
        re.delete()
        return redirect('reportes')

def mapa_piso1(request):
    return render(request, 'mapa/piso1.html')

def mapa_piso2(request):
    return render(request, 'mapa/piso2.html')

def mapa_piso0(request):
    return render(request, 'mapa/piso-1.html')

def registrar(request):
    if request.method == 'POST':
        form = Registroform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('postlogin')
    else:
        form = Registroform()
    return render(request, 'registro.html', {'form': form})

@login_required
def postlogin(request):
    nuevo_reporte=request.session.pop('nuevo_reporte',False) # Ve si hay nuevo reporte
    reportes = reporte.objects.filter(completado=False).order_by('-id') #para mostrar lista de reportes
    return render(request, 'postlogin.html', {'r': reportes, 'nuevo_reporte':nuevo_reporte})