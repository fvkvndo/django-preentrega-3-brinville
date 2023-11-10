from django.urls import path
from control_entrega.views import (
    lista_medicos, lista_internaciones, lista_pacientes, agregar_internacion, agregar_medico, agregar_paciente, buscar_medicos
)

urlpatterns = [
    path("medicos/", lista_medicos, name="lista_medicos"),
    path("pacientes/", lista_pacientes, name="lista_pacientes"),
    path("internaciones/", lista_internaciones, name="lista_internaciones"),
    path("agregar-medico/", agregar_medico, name="agregar_medico"),
    path("agregar-paciente/", agregar_paciente, name="agregar_paciente"),
    path("agregar-internacion/", agregar_internacion, name="agregar_internacion"),
    path("buscar-medicos/", buscar_medicos, name="buscar_medicos"),
]
