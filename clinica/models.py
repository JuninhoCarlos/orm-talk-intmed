from django.db import models


class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100)
    cep = models.CharField(max_length=100, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Clinica(models.Model):
    nome = models.CharField(max_length=100)
    medicos = models.ManyToManyField(Medico, related_name="clinicas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    juridico = models.ForeignKey("Juridico", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Juridico(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
