from django.db import models

# Create your models here.
class Tienda(models.Model):
    id_tienda=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    telefono=models.PositiveIntegerField()
    correo_electronico=models.EmailField(max_length=50)
    horario=models.CharField(max_length=100)
    tipo_de_productos=models.CharField(max_length=50)

    
    def __str__(self):
        return self.nombre