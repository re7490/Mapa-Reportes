from django.urls import path
from . import views

urlpatterns = [
    path('piso-1/', views.mapa_piso0, name='piso-1'),
    path('piso1/', views.mapa_piso1, name='piso1'),
    path('piso2/', views.mapa_piso2, name='piso2'),
    path('piso4/', views.mapa_piso4, name='piso4'),
    
]