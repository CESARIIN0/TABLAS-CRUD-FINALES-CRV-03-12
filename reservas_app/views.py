from django.shortcuts import render, redirect
from .models import Reserva

# Create your views here.
def inicio_vistaReserva(request):
    lasreservas = Reserva.objects.all()
    return render(request, "gestionarReserva.html", {"misreservas": lasreservas})

def registrarReserva(request):
    id_reserva = request.POST["txtcodigo"]
    id_cliente = request.POST["txtidcliente"]
    fecha_reserva = request.POST["datelafecha"]
    numero_reserva = request.POST["txtnumero"]
    hora_llegada = request.POST["txthoraLlegada"]
    hora_salida = request.POST["txthoraSalida"]
    id_mesa = request.POST["txtidmesa"]

    Reserva.objects.create(
        id_reserva=id_reserva,
        id_cliente=id_cliente,
        fecha_reserva=fecha_reserva,
        numero_reserva=numero_reserva,
        hora_llegada=hora_llegada,
        hora_salida=hora_salida,
        id_mesa=id_mesa,
    )  # GUARDA EL REGISTRO
    return redirect("reserva")

def seleccionarReserva(request, codigo):
    reserva = Reserva.objects.get(id_reserva=codigo)
    fecha_reserva = reserva.fecha_reserva.strftime('%Y-%m-%d')
    return render(request, "editarReserva.html", {"misreservas": reserva, "fecha_reserva": fecha_reserva})

def editarReserva(request):
    id_reserva = request.POST["txtcodigo"]
    id_cliente = request.POST["txtidcliente"]
    fecha_reserva = request.POST["datelafecha"]
    numero_reserva = request.POST["txtnumero"]
    hora_llegada = request.POST["txthoraLlegada"]
    hora_salida = request.POST["txthoraSalida"]
    id_mesa = request.POST["txtidmesa"]

    reserva = Reserva.objects.get(id_reserva=id_reserva)
    reserva.id_cliente = id_cliente
    reserva.fecha_reserva = fecha_reserva
    reserva.numero_reserva = numero_reserva
    reserva.hora_llegada = hora_llegada
    reserva.hora_salida = hora_salida
    reserva.id_mesa = id_mesa
    reserva.save()  # GUARDA EL REGISTRO ACTUALIZADO

    return redirect("reserva")

def borrarReserva(request, codigo):
    reserva = Reserva.objects.get(id_reserva=codigo)
    reserva.delete()  # BORRA EL REGISTRO
    return redirect("reserva")
