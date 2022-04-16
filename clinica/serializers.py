from rest_framework import serializers

from .models import Clinica, Juridico, Medico


class JuridicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juridico()
        fields = ("id", "nome", "cnpj", "responsavel")


class ClinicaSerializer(serializers.ModelSerializer):
    juridico = JuridicoSerializer()

    class Meta:
        model = Clinica
        fields = ("id", "nome", "juridico")


class MedicoSerializer(serializers.ModelSerializer):
    clinicas = ClinicaSerializer(many=True)

    class Meta:
        model = Medico
        fields = ("id", "crm", "nome", "clinicas")
