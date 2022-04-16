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


class SimpleMedicoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    crm = serializers.CharField(max_length=100)
    nome = serializers.CharField(max_length=100)
