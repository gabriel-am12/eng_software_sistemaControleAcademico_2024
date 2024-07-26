from django.db import models

class Estudante(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    pre_requisitos = models.TextField(blank=True)
    programa = models.TextField()

    def __str__(self):
        return self.nome

class Professor(models.Model):
    id_professor = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome
