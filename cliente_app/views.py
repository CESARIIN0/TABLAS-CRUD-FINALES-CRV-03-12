from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.
def inicio_vistaClientes(request):
    losclientes = Cliente.objects.all()
    return render(request, "gestionarClientes.html", {"misclientes": losclientes})

def registrarCliente(request):
    id_cliente = request.POST["txtid_cliente"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    correo_electronico = request.POST["txtcorreo_electronico"]
    direccion = request.POST["txtdireccion"]
    hora_que_reserva = request.POST["txthora_que_reserva"]
    hora_salida = request.POST["txthora_salida"]

    nuevo_cliente = Cliente.objects.create(
        id_cliente=id_cliente,
        nombre=nombre,
        telefono=telefono,
        correo_electronico=correo_electronico,
        direccion=direccion,
        hora_que_reserva=hora_que_reserva,
        hora_salida=hora_salida,
    )
    nuevo_cliente.save()
    return redirect("inicio_vistaClientes")

def seleccionarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    return render(request, "editarClientes.html", {"misclientes": cliente})

def editarCliente(request):
    id_cliente = request.POST["txtid_cliente"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    correo_electronico = request.POST["txtcorreo_electronico"]
    direccion = request.POST["txtdireccion"]
    hora_que_reserva = request.POST["txthora_que_reserva"]
    hora_salida = request.POST["txthora_salida"]

    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre = nombre
    cliente.telefono = telefono
    cliente.correo_electronico = correo_electronico
    cliente.direccion = direccion
    cliente.hora_que_reserva = hora_que_reserva
    cliente.hora_salida = hora_salida
    cliente.save()
    return redirect("inicio_vistaClientes")

def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("inicio_vistaClientes")
