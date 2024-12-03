from django.shortcuts import render, redirect
from .models import Plato

def inicio_vistaPlato(request):
    losplatos = Plato.objects.all()
    return render(request, "gestionarPlato.html", {"misplatos": losplatos})

def registrarPlato(request):
    id_plato = request.POST["txtid_plato"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["numprecio"]
    tipo = request.POST["txttipo"]
    fechasolicitud = request.POST["txtfechasolicitud"]
    fecha_entrega = request.POST["txtfecha_entrega"]
    Cuantos_Platos=request.POST["numplatos"]
    
    Plato.objects.create(
        id_plato=id_plato,
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        tipo=tipo,
        fechasolicitud=fechasolicitud,
        fecha_entrega=fecha_entrega,
        Cuantos_Platos=Cuantos_Platos,
    )
    return redirect("inicio_vistaPlato")

def seleccionarPlato(request, id_plato):
    plato = Plato.objects.get(id_plato=id_plato)
    fecha_fin=plato.fechasolicitud.strftime('%Y-%m-%d')
    fecha_inicio=plato.fecha_entrega.strftime('%Y-%m-%d')
    return render(request,"editarPlato.html",{"misplatos":plato, "misplatos" : plato, "fecha_fin" : fecha_fin, "fecha_inicio" : fecha_inicio})

def editarPlato(request):
    id_plato = request.POST["txtid_plato"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["numprecio"]
    tipo = request.POST["txttipo"]
    fechasolicitud = request.POST["txtfechasolicitud"]
    fecha_entrega = request.POST["txtfecha_entrega"]
    Cuantos_Platos=request.POST["numplatos"]

    plato = Plato.objects.get(id_plato=id_plato)
    plato.nombre = nombre
    plato.descripcion = descripcion
    plato.precio = precio
    plato.tipo = tipo
    plato.fechasolicitud = fechasolicitud
    plato.fecha_entrega = fecha_entrega
    plato.Cuantos_Platos = Cuantos_Platos
    plato.save()
    return redirect("inicio_vistaPlato")

def borrarPlato(request, id_plato):
    plato = Plato.objects.get(id_plato=id_plato)
    plato.delete()
    return redirect("inicio_vistaPlato")
