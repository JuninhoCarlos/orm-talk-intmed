from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Clinica, Medico
from .serializers import (
    ClinicaSerializer,
    MedicoSerializer,
    SimpleMedicoSerializer,
)
from .utils.data_structure import tuple_to_dict
from .utils.queries import CountQueries, print_queries
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


class SimpleMedicoAPIView(ListAPIView):
    serializer_class = SimpleMedicoSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Medico.objects.all()

    fields = ("id", "nome", "crm")
    defer_fields = (
        "created_at",
        "updated_at",
        "ativo",
        "cep",
        "email",
        "telefone",
        "nome",
    )

    @print_queries
    @timed
    def list(self, request):

        # queryset = self.get_queryset()
        # serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)
        # return self.values_list_sample()
        # return self.values_sample()
        # return self.only_sample()
        return self.defer_sample()

    def values_sample(self):
        """
        This is a sample of how to use values()
        """
        queryset = self.get_queryset()
        queryset_data = queryset.values(*self.fields)
        serializer = self.get_serializer(queryset_data, many=True)
        return Response(serializer.data)

    def values_list_sample(self):
        """
        This is a sample of how to use values_list()
        """
        queryset = self.get_queryset()
        queryset_tuple = queryset.values_list(*self.fields)
        queryset_data = tuple_to_dict(queryset_tuple, self.fields)

        serializer = self.get_serializer(queryset_data, many=True)
        return Response(serializer.data)

    def only_sample(self):
        """
        This is a sample of how to use only()
        """
        queryset = self.get_queryset()
        queryset_data = queryset.only(*self.fields)
        serializer = self.get_serializer(queryset_data, many=True)
        return Response(serializer.data)

    def defer_sample(self):
        """
        This is a sample of how to use only()
        """
        queryset = self.get_queryset()
        queryset_data = queryset.defer(*self.defer_fields)
        serializer = self.get_serializer(queryset_data, many=True)
        return Response(serializer.data)
