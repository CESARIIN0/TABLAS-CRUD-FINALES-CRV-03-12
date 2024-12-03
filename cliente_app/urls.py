from django.urls import path
from cliente_app import views

urlpatterns = [
    path("inicio_vistaClientes", views.inicio_vistaClientes, name="inicio_vistaClientes"),
    path("registrarCliente/", views.registrarCliente, name="registrarCliente"),
    path("seleccionarCliente/<int:id_cliente>", views.seleccionarCliente, name="seleccionarCliente"),
    path("editarCliente/", views.editarCliente, name="editarCliente"),
    path("borrarCliente/<int:id_cliente>", views.borrarCliente, name="borrarCliente"),
]
