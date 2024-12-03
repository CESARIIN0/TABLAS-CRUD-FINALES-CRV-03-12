from django.urls import path
from plato_app import views

urlpatterns = [
    path("inicio_vistaPlato", views.inicio_vistaPlato, name="inicio_vistaPlato"),
    path("registrarPlato/", views.registrarPlato, name="registrarPlato"),
    path("seleccionarPlato/<int:id_plato>", views.seleccionarPlato, name="seleccionarPlato"),
    path("editarPlato/", views.editarPlato, name="editarPlato"),
    path("borrarPlato/<int:id_plato>", views.borrarPlato, name="borrarPlato"),
]
