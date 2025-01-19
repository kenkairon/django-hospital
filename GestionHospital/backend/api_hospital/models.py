from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido}"


class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='citas')
    fecha_hora = models.DateTimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=15, choices=[('Pendiente', 'Pendiente'), ('Completada', 'Completada'), ('Cancelada', 'Cancelada')])

    def __str__(self):
        return f"Cita de {self.paciente} con {self.medico} el {self.fecha_hora}"