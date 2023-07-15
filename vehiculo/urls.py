from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("vehiculo/add", views.agregar_vehiculo, name="agregar_vehiculo"),
    path("vehiculo/registro-usuario", views.registro, name="registro_usuario"),
    path("vehiculo/login", views.login_view, name="login"),
]