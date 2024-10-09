from django.db import models

class Horario(models.Model):
    horario = models.TimeField(unique=True)

    def __str__(self):
        return str(self.horario)

class Agendamento(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.data} {self.horario}"

class DiaDisponivel(models.Model):
    data = models.DateField(unique=True)

    def __str__(self):
        return str(self.data)