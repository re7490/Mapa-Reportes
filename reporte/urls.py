from django.urls import path
from . import views
from .views import registrar
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('piso-1/', views.mapa_piso0, name='piso-1'),
    path('piso1/', views.mapa_piso1, name='piso1'),
    path('piso2/', views.mapa_piso2, name='piso2'),
    path('registrar/', registrar, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', success_url='/postlogin/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('postlogin/', views.postlogin,name='postlogin'),
    path('crear_reporte/', views.crear_reporte, name='crear_reporte'),
]