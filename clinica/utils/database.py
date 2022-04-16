from random import randint

from faker import Faker
from tqdm import tqdm

from clinica.models import Clinica, Juridico, Medico


def populate_medico(num_medicos=100):
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


def populate_clinica(
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
        random_medico = randint(1, 15)
        select_medicos = []

        for j in range(random_medico):
            medico_id = randint(1, num_medicos)
            select_medicos.append(medico_id)

        medicos = Medico.objects.filter(id__in=select_medicos)

        for medico in medicos:
            clinica.medicos.add(medico)

        clinica.save()
