from django import forms

class MedicoFormulario(forms.Form):
     nombre = forms.CharField(required=True, max_length=64)
     apellido = forms.CharField(max_length=100)
     especialidad = forms.CharField(required=True, max_length=64)

class PacienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    edad = forms.CharField(max_length=100)
    historial_medico = forms.CharField(max_length=100)

class InternacionFormulario(forms.Form):
    medico = forms.CharField(max_length=100)
    paciente = forms.CharField(max_length=100)
    fecha_entrada = forms.IntegerField(required=True, max_value=80000)
    fecha_salida = forms.IntegerField(required=True, max_value=80000)
