from django.urls import path
from . import views

app_name = 'formularios'

urlpatterns = [
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear_exitoso/', views.crear_exitoso, name='crear_exitoso'),
    path('<id>/borrar/', views.eliminar_usuario, name='eliminar_usuario'),
]