from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Medico
from .serializers import MedicoSerializer
from .utils.queries import CountQueries
from .utils.time import timed


class MedicoAPIView(ListAPIView):
    serializer_class = MedicoSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Medico.objects.all()

    @timed
    def list(self, request):
        with CountQueries():
            queryset = self.get_queryset()
            serializer = MedicoSerializer(queryset, many=True)
            return Response(serializer.data)
