from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    telefono=models.PositiveIntegerField()
    correo=models.EmailField(max_length=50)
    cargo=models.CharField(max_length=50)
    fecha_ingreso=models.DateField(null=False,blank=False)
    hora_llegada=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre