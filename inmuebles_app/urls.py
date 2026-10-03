from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('nuevo_inmueble/', views.nuevo_inmueble_view, name='nuevo_inmueble'),
    path('lista_inmuebles/', views.lista_inmuebles_view, name='lista_inmuebles'),
    path('eliminar_inmueble/<int:inmueble_id>/', views.eliminar_inmueble_view, name='eliminar_inmueble'),
    path('actualizar_inmueble/<int:inmueble_id>/', views.actualizar_inmueble_view, name='actualizar_inmueble'),
    path('catalogo_inmuebles/', views.catalogo_inmuebles_view, name='catalogo_inmuebles'),
]