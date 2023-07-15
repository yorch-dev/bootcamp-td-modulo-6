from django.shortcuts import render
from .forms import VehiculoForm
from django.contrib import messages

# Create your views here.
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