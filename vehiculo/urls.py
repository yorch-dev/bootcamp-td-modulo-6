from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("vehiculo/add", views.agregar_vehiculo, name="agregar_vehiculo"),
    path("vehiculo/registro-usuario", views.registro, name="registro_usuario"),
    path("vehiculo/login", views.CustomLoginView.as_view(), name="login"),
    path("vehiculo/logout", views.CustomLogoutView.as_view(), name="logout"),
]