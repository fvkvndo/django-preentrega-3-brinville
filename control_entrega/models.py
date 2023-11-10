from django.db import models

class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
         return f"{self.nombre} {self.apellido}"

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    historial_medico = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Internacion(models.Model):
    medico = models.CharField(max_length=100)
    paciente = models.CharField(max_length=100)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.paciente} internado por {self.medico}'
