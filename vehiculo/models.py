from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True

class Vehiculo(models.Model):
    modelos = (
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota')
    )
    categorias = (
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga')
    )

    marca = models.CharField(max_length=20, choices=modelos, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=categorias, default='Particular')
    precio = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ('visualizar_catalogo', 'Puede visualizar'),
        )

    def __str__(self):
        return self.marca + " " + self.modelo + " serial carrocería: " + self.serial_carroceria
    