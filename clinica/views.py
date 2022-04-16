from rest_framework.generics import ListAPIView

from .models import Medico
from .serializers import MedicoSerializer


class MedicoAPIView(ListAPIView):
    serializer_class = MedicoSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Medico.objects.all()
