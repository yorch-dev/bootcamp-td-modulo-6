from django.shortcuts import render
from .forms import VehiculoForm
from django.contrib import messages
from django.views import generic
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.contenttypes.models import ContentType
from .models import Vehiculo
from django.contrib.auth import login
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'vehiculo/index.html')

def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vehículo ingresado correctamente")
            ctx = {
                'form' : VehiculoForm()
            }
            return render(request, 'vehiculo/agregar.html', ctx)
        else:
            ctx = {
                'form' : form
            }
            return render(request, 'vehiculo/agregar.html', ctx)
    else:
        ctx = {
            'form' : VehiculoForm()
        }
        return render(request, 'vehiculo/agregar.html', ctx)

def registro(request):
    url_inicio = reverse_lazy('index')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(Vehiculo)
            ver_contenido = Permission.objects.get(
                codename = 'visualizar_catalogo',
                content_type = content_type
            )
            user = form.save()
            user.user_permissions.add(ver_contenido)
            login(request, user)
            messages.success(request, 'Registrado satisfactoriamente')
            return HttpResponseRedirect(url_inicio)
        else:
            messages.error(request, 'Registro inválido, algunos datos ingresados no son correctos')
            form = UserRegisterForm(request.POST)
            ctx = {'form' : form}
            return render(request, 'registration/registro.html', ctx)
    form = UserRegisterForm()
    ctx = {'form' : form}
    return render(request, 'registration/registro.html', ctx)

def login_view(request):
    url_inicio = reverse_lazy('index')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Sesión iniciada como: {username}')
                return HttpResponseRedirect(url_inicio)
            else:
                messages.error(request, 'Error en usuario o contraseña')
                form = AuthenticationForm(request, data=request.POST)
                ctx = {
                    'form' : form
                }
                return render(request, 'registration/login.html', ctx)
        else:
            messages.error(request, 'Ingreso inválido, algunos datos ingresados no son correctos')
            form = UserRegisterForm(request.POST)
            ctx = {
                'form' : form
            }
            return render(request, 'registration/login.html', ctx)
    form = AuthenticationForm()
    ctx = {
        'form' : form
    }
    return render(request, 'registration/login.html', ctx)