from django.urls import path
from reservas_app import views

urlpatterns = [
    path("reserva", views.inicio_vistaReserva, name="reserva"),
    path("registrarReserva/", views.registrarReserva, name="registrarReserva"),
    path("seleccionarReserva/<codigo>", views.seleccionarReserva, name="seleccionarReserva"),
    path("editarReserva/", views.editarReserva, name="editarReserva"),
    path("borrarReserva/<codigo>", views.borrarReserva, name="borrarReserva"),
]
