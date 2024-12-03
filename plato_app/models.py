from django.db import models

# Create your models here.
class Plato(models.Model):
    id_plato=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=300)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    tipo=models.CharField(max_length=50)
    fechasolicitud=models.DateField(null=False,blank=False)
    fecha_entrega=models.DateField(null=False,blank=False)
    Cuantos_Platos=models.IntegerField()
    def __str__(self):
        return self.nombre