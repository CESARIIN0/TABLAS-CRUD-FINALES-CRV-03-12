from django.shortcuts import render, redirect
from .models import Tienda

# Create your views here.
def inicio_vistaTienda(request):
    lostiendas = Tienda.objects.all()
    return render(request, "gestionarTiendas.html", {"mistiendas": lostiendas})

def registrarTienda(request):
    if request.method == 'POST':
        id_tienda = request.POST["txtid_tienda"]
        nombre = request.POST["txtnombre"]
        direccion = request.POST["txtdireccion"]
        telefono = request.POST["numtelefono"]
        correo_electronico = request.POST["txtcorreo_electronico"]
        horario = request.POST["txthorario"]
        tipo_de_productos = request.POST["txttipo_de_productos"]

        Tienda.objects.create(
            id_tienda=id_tienda,
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            correo_electronico=correo_electronico,
            horario=horario,
            tipo_de_productos=tipo_de_productos
        )
    return redirect("inicio_vistaTienda")

def seleccionarTienda(request, id_tienda):
    tienda = Tienda.objects.get(id_tienda=id_tienda)
    return render(request, "editarTienda.html", {"mistiendas": tienda})

def editarTienda(request):
    if request.method == 'POST':
        id_tienda = request.POST["txtid_tienda"]
        nombre = request.POST["txtnombre"]
        direccion = request.POST["txtdireccion"]
        telefono = request.POST["numtelefono"]
        correo_electronico = request.POST["txtcorreo_electronico"]
        horario = request.POST["txthorario"]
        tipo_de_productos = request.POST["txttipo_de_productos"]

        tienda = Tienda.objects.get(id_tienda=id_tienda)
        tienda.nombre = nombre
        tienda.direccion = direccion
        tienda.telefono = telefono
        tienda.correo_electronico = correo_electronico
        tienda.horario = horario
        tienda.tipo_de_productos = tipo_de_productos
        tienda.save()

    return redirect("inicio_vistaTienda")

def borrarTienda(request, id_tienda):
    tienda = Tienda.objects.get(id_tienda=id_tienda)
    tienda.delete()
    return redirect("inicio_vistaTienda")
