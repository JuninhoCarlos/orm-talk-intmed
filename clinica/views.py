from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Clinica, Medico
from .serializers import ClinicaSerializer, MedicoSerializer
from .utils.queries import CountQueries
from .utils.time import timed


class MedicoAPIView(ListAPIView):
    serializer_class = MedicoSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Medico.objects.prefetch_related("clinicas", "clinicas__juridico").all()

    @timed
    def list(self, request):
        with CountQueries():
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)


class ClinicaAPIView(ListAPIView):
    serializer_class = ClinicaSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Clinica.objects.select_related("juridico").all()

    @timed
    def list(self, request):
        with CountQueries():
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
