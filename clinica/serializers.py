from rest_framework import serializers

from .models import Clinica, Juridico, Medico


class JuridicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juridico()
        fields = ("id", "nome", "cnpj", "responsavel")


# class MedicoClinicaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Medico
#         fields = ("id", "crm", "nome")


class ClinicaSerializer(serializers.ModelSerializer):
    juridico = JuridicoSerializer()
    medicos_ativos = serializers.SerializerMethodField()
    medicos_total = serializers.SerializerMethodField()

    def get_medicos_ativos(self, clinica):
        return len([medico for medico in clinica.medicos.all() if medico.ativo])

    def get_medicos_total(self, clinica):
        return len([medico for medico in clinica.medicos.all()])

    class Meta:
        model = Clinica
        fields = (
            "id",
            "nome",
            "juridico",
            "medicos_ativos",
            "medicos_total",
        )


class ClinicaMedicoSerializer(serializers.ModelSerializer):
    juridico = JuridicoSerializer()

    class Meta:
        model = Clinica
        fields = (
            "id",
            "nome",
            "juridico",
        )


class MedicoSerializer(serializers.ModelSerializer):
    clinicas = ClinicaMedicoSerializer(many=True)

    class Meta:
        model = Medico
        fields = ("id", "crm", "nome", "clinicas")


class SimpleMedicoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    crm = serializers.CharField(max_length=100)
    nome = serializers.CharField(max_length=100)
