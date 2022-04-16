from django.core.management.base import BaseCommand, CommandError

from clinica.utils.database import populate_clinica, populate_medico


class Command(BaseCommand):
    help = "Populates the database with fake data"

    def add_arguments(self, parser):
        parser.add_argument("number_of_rows", type=int)

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
        populate_medico(number_of_rows)

        self.stdout.write(self.style.SUCCESS("Populating Clinica Table"))
        populate_clinica(number_of_rows, number_of_rows)

        self.stdout.write(self.style.SUCCESS("Successfully populated the database "))
