from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    telefono=models.PositiveIntegerField()
    correo_electronico=models.EmailField(max_length=50)
    direccion=models.CharField(max_length=100)
    hora_que_reserva=models.CharField(max_length=50)
    hora_salida=models.CharField(max_length=50)

    
    def __str__(self):
        return self.nombre