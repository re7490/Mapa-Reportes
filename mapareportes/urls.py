"""
URL configuration for mapareportes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reporte import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('reporte.urls')),
    path('signup/', views.signup, name='signup'),
    path('crear_reporte/', views.crear_reporte, name='crear_reporte'),
    path('reportes/', views.reportes, name='reportes'),
    path('reportes/<int:id>/', views.reporte_, name='reporte_'),
    path('reportes/<int:id>/borrar_reporte', views.borrar_reporte, name='borrar_reporte'),
    path('piso-1/', views.mapa_piso0, name='piso-1'),
    path('piso1/', views.mapa_piso1, name='piso1'),
    path('piso2/', views.mapa_piso2, name='piso2'),
    path('piso4/', views.mapa_piso4, name='piso4'),
        
]
