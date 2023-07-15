from django.shortcuts import render
from .forms import VehiculoForm
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Vehiculo
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView

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
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
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

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, f'Sesión iniciada como: {form.cleaned_data.get("username")}')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error en usuario o contraseña')
        return super().form_invalid(form)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
        return super().dispatch(request, *args, **kwargs)