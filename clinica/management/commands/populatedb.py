from random import randint

from faker import Faker
from tqdm import tqdm

from django.core.management.base import BaseCommand, CommandError

from clinica.models import Clinica, Juridico, Medico


class Command(BaseCommand):
    help = "Populates the database with fake data"

    def add_arguments(self, parser):
        parser.add_argument("number_of_rows", type=int)

    def _populate_medico(self, num_medicos=100):
        faker = Faker()
        for i in tqdm(range(num_medicos)):
            medico = Medico(
                nome=faker.name(),
                crm=faker.random_number(digits=5),
                telefone=faker.phone_number(),
                email=faker.email(),
                cep=faker.postcode(),
                ativo=faker.boolean(),
            )
            medico.save()

    def _populate_clinica(
        self,
        num_medicos,
        num_clinicas=100,
    ):
        assert num_medicos > 30, "num_medicos must be greater than 30"

        faker = Faker()
        for i in tqdm(range(num_clinicas)):
            # Juridico for the clinic
            juridico = Juridico(
                nome=faker.name(),
                cnpj=faker.random_number(digits=14),
                responsavel=faker.name(),
            )
            juridico.save()

            clinica = Clinica(
                nome=faker.company(),
                juridico=juridico,
            )
            clinica.save()
            # the number of doctors in a clinic ranges from 1 to 30
            random_medico = randint(1, 30)
            select_medicos = []
            for j in range(random_medico):
                medico_id = randint(1, num_medicos)
                medico = Medico.objects.get(id=medico_id)
                clinica.medicos.add(medico)

            clinica.save()

    def handle(self, *args, **options):
        number_of_rows = options["number_of_rows"]
        self.stdout.write(
            self.style.SUCCESS(
                "Populating database with fake data. (number_of_rows={})".format(
                    number_of_rows
                )
            )
        )

        self.stdout.write(self.style.SUCCESS("Populating Medico Table"))
        self._populate_medico(number_of_rows)

        self.stdout.write(self.style.SUCCESS("Populating Clinica Table"))
        self._populate_clinica(number_of_rows, number_of_rows)

        self.stdout.write(self.style.SUCCESS("Successfully populated the database "))
