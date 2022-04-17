from rest_framework.generics import ListAPIView

from .models import Clinica, Medico
from .serializers import ClinicaSerializer, MedicoSerializer


class MedicoAPIView(ListAPIView):
    serializer_class = MedicoSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Medico.objects.all()


class ClinicaAPIView(ListAPIView):
    serializer_class = ClinicaSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Clinica.objects.all()
