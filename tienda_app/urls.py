from django.urls import path
from tienda_app import views

urlpatterns = [
    path("inicio_vistaTienda", views.inicio_vistaTienda, name="inicio_vistaTienda"),
    path("registrarTienda/", views.registrarTienda, name="registrarTienda"),
    path("seleccionarTienda/<id_tienda>", views.seleccionarTienda, name="seleccionarTienda"),
    path("editarTienda/", views.editarTienda, name="editarTienda"),
    path("borrarTienda/<id_tienda>", views.borrarTienda, name="borrarTienda"),
]
