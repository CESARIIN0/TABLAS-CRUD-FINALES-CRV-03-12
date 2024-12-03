from django.urls import path
from empleado_app import views

urlpatterns = [
    path("inicio_vistaEmpleado", views.inicio_vistaEmpleado, name="inicio_vistaEmpleado"),
    path("registrarEmpleado/", views.registrarEmpleado, name="registrarEmpleado"),
    path("seleccionarEmpleado/<int:id_empleado>", views.seleccionarEmpleado, name="seleccionarEmpleado"),
    path("editarEmpleado/", views.editarEmpleado, name="editarEmpleado"),
    path("borrarEmpleado/<int:id_empleado>", views.borrarEmpleado, name="borrarEmpleado"),
]
