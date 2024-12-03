from django.shortcuts import render, redirect
from .models import Empleado

def inicio_vistaEmpleado(request):
    empleados = Empleado.objects.all()
    return render(request, "gestionarEmpleado.html", {"misempleados": empleados})

def registrarEmpleado(request):
    id_empleado = request.POST["txtid_empleado"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    correo = request.POST["txtcorreo"]
    cargo = request.POST["txtcargo"]
    fecha_ingreso = request.POST["txtfecha_ingreso"]
    hora_llegada = request.POST["txthora_llegada"]

    Empleado.objects.create(
        id_empleado=id_empleado,
        nombre=nombre,
        telefono=telefono,
        correo=correo,
        cargo=cargo,
        fecha_ingreso=fecha_ingreso,
        hora_llegada=hora_llegada,
    )
    return redirect("inicio_vistaEmpleado")

def seleccionarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    fecha_fin=empleado.fecha_ingreso.strftime('%Y-%m-%d')
    return render(request,"editarEmpleado.html",{"misempleados":empleado, "misempleados" : empleado, "fecha_fin" : fecha_fin})

def editarEmpleado(request):
    id_empleado = request.POST["txtid_empleado"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    correo = request.POST["txtcorreo"]
    cargo = request.POST["txtcargo"]
    fecha_ingreso = request.POST["txtfecha_ingreso"]
    hora_llegada = request.POST["txthora_llegada"]

    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.nombre = nombre
    empleado.telefono = telefono
    empleado.correo = correo
    empleado.cargo = cargo
    empleado.fecha_ingreso = fecha_ingreso
    empleado.hora_llegada = hora_llegada
    empleado.save()
    return redirect("inicio_vistaEmpleado")

def borrarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete()
    return redirect("inicio_vistaEmpleado")
