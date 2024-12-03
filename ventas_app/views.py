from django.shortcuts import render, redirect
from .models import Ventas

# Create your views here.
def inicio_vistaVentas(request):
    lasventas = Ventas.objects.all()
    return render(request, "gestionarVentas.html", {"misventas": lasventas})

def registrarVenta(request):
    id_venta = request.POST["txtid_venta"]
    id_empleado = request.POST["txtid_empleado"]
    id_cliente = request.POST["txtid_cliente"]
    fecha_venta = request.POST["txtfecha_venta"]
    id_plato = request.POST["txtid_plato"]
    total_venta = request.POST["txttotal_venta"]
    descripcion = request.POST["txtdescripcion"]

    nueva_venta = Ventas.objects.create(
        id_venta=id_venta,
        id_empleado=id_empleado,
        id_cliente=id_cliente,
        fecha_venta=fecha_venta,
        id_plato=id_plato,
        total_venta=total_venta,
        descripcion=descripcion,
    )
    nueva_venta.save()
    return redirect("inicio_vistaVentas")

def seleccionarVenta(request, id_venta):
    venta = Ventas.objects.get(id_venta=id_venta)
    fecha_fin=venta.fecha_venta.strftime('%Y-%m-%d')
    return render(request,"editarVentas.html",{"misventas":venta, "misventas" : venta, "fecha_fin" : fecha_fin})


def editarVenta(request):
    id_venta = request.POST["txtid_venta"]
    id_empleado = request.POST["txtid_empleado"]
    id_cliente = request.POST["txtid_cliente"]
    fecha_venta = request.POST["txtfecha_venta"]
    id_plato = request.POST["txtid_plato"]
    total_venta = request.POST["txttotal_venta"]
    descripcion = request.POST["txtdescripcion"]

    venta = Ventas.objects.get(id_venta=id_venta)
    venta.id_empleado = id_empleado
    venta.id_cliente = id_cliente
    venta.fecha_venta = fecha_venta
    venta.id_plato = id_plato
    venta.total_venta = total_venta
    venta.descripcion = descripcion
    venta.save()
    return redirect("inicio_vistaVentas")

def borrarVenta(request, id_venta):
    venta = Ventas.objects.get(id_venta=id_venta)
    venta.delete()
    return redirect("inicio_vistaVentas")
