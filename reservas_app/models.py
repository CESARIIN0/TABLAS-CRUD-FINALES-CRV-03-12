from django.db import models

# Create your models here.
class Reserva(models.Model):
    id_reserva = models.PositiveIntegerField(primary_key=True)
    id_cliente = models.PositiveIntegerField()
    fecha_reserva = models.DateField(null=False, blank=False)
    numero_reserva = models.PositiveBigIntegerField()
    hora_llegada = models.CharField(max_length=100)
    hora_salida = models.CharField(max_length=100)
    id_mesa = models.PositiveIntegerField()

    def __str__(self):
        return self.id_reserva
