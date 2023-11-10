from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q
from control_entrega.models import Medico, Paciente, Internacion
from control_entrega.forms import MedicoFormulario, PacienteFormulario, InternacionFormulario

def lista_medicos(request):
    contexto = {
        "medicos": Medico.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_entrega/lista_medicos.html',
        context=contexto,
    )
    return http_response

# Repite un patrón similar para Paciente e Internacion
def lista_pacientes(request):
    contexto = {
        "pacientes": Paciente.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_entrega/lista_pacientes.html',
        context=contexto,
    )
    return http_response

def lista_internaciones(request):
    contexto = {
        "internaciones": Internacion.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_entrega/lista_internaciones.html',
        context=contexto,
    )
    return http_response

# Vista para agregar un nuevo médico
def agregar_medico(request):
    if request.method == 'POST':
        form = MedicoFormulario(request.POST)
        if form.is_valid():
                data = formulario.cleaned_data  # es un diccionario
                nombre = data["nombre"]
                apellido = data["apellido"]
                especialidad = data["especialidad"]
                # creo un curso en memoria RAM
                medico = Medico(nombre=nombre, apellido=apellido, especialidad=especialidad)
                # Lo guardan en la Base de datos
                medico.save()

                # Redirecciono al usuario a la lista de cursos
                url_exitosa = reverse('lista_medicos')  # estudios/cursos/
                return redirect(url_exitosa)
        else:  # GET
        # Descargar formulario inicial
            formulario = MedicoFormulario()
            http_response = render(
            request=request,
            template_name='control_entrega/agregar_medico.html',
            context={'formulario': formulario}
    )
    return http_response

# Vista para agregar un nuevo paciente (repite un patrón similar para Internacion)
def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteFormulario(request.POST)
        if form.is_valid():
                data = formulario.cleaned_data  # es un diccionario
                nombre = data["nombre"]
                apellido = data["apellido"]
                edad = data["edad"]
                historial_medico = data["historial"]
                # creo un curso en memoria RAM
                paciente = Paciente(nombre=nombre, apellido=apellido, edad=edad, historial_medico=historial_medico)
                # Lo guardan en la Base de datos
                paciente.save()

                # Redirecciono al usuario a la lista de cursos
                url_exitosa = reverse('lista_pacientes')  # estudios/cursos/
                return redirect(url_exitosa)
        else:  # GET
        # Descargar formulario inicial
            formulario = PacienteFormulario()
            http_response = render(
            request=request,
            template_name='control_entrega/agregar_paciente.html',
            context={'formulario': formulario}
    )
    return http_response

def agregar_internacion(request):
    if request.method == 'POST':
        form = InternacionFormulario(request.POST)
        if form.is_valid():
                data = formulario.cleaned_data  # es un diccionario
                medico = data["medico"]
                paciente = data["paciente"]
                fecha_entrada = data["fecha_entrada"]
                fecha_salida = data["fecha_salida"]
                # creo un curso en memoria RAM
                internacion = Internacion(medico=medico, paciente=paciente, fecha_entrada=fecha_entrada, fecha_salida=fecha_salida) 
                # Lo guardan en la Base de datos
                internacion.save()

                # Redirecciono al usuario a la lista de cursos
                url_exitosa = reverse('lista_internacion')  # estudios/cursos/
                return redirect(url_exitosa)
        else:  # GET
        # Descargar formulario inicial
            formulario = InternacionFormulario()
            http_response = render(
            request=request,
            template_name='control_entrega/agregar_internacion.html',
            context={'formulario': formulario}
    )
    return http_response

def buscar_medicos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        # cursos = Curso.objects.filter(comision__contains=busqueda)
        # Ejemplo filtro avanzado
        medicos = Medico.objects.filter(
            Q(apellido__icontains=busqueda) | Q(especialidad__contains=busqueda)
        )

        contexto = {
            "medicos": medicos,
        }
        http_response = render(
            request=request,
            template_name='control_entrega/lista_medicos.html',
            context=contexto,
        )
        return http_response