from rest_framework.test import APIClient, APITestCase

from django.urls import reverse

from .utils.database import populate_clinica, populate_medico


class TestClinica(APITestCase):
    def setUp(self):
        self.client = APIClient()

        populate_medico(num_medicos=40)
        populate_clinica(num_medicos=40, num_clinicas=10)

    def test_number_of_medico_queries(self):
        """
        Test the number of queries for list of doctors
        """
        url = reverse("medicos")

        with self.assertNumQueries(3):
            response = self.client.get(reverse("medicos"))

        # is that enough?
        # The answer is no.
        # Prova por indução
        populate_medico(num_medicos=40)
        populate_clinica(num_medicos=40, num_clinicas=10)

        with self.assertNumQueries(3):
            response = self.client.get(reverse("medicos"))
