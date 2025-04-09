from django.core.management.base import BaseCommand
import csv
from ...models import Person
print(">>> Custom commands loaded")
"""20366 records are inserted in db and I have stopped import as there are 12,000,000 records"""
class Command(BaseCommand):
    help = 'Import data from name.basics.tsv'  # This is a simple description that will appear when we will run python manage.py help import_name_basic_tsc_table

    def add_arguments(self, parser):
        parser.add_argument('tsv_file', type=str)

    """This line defines a required positional argument called tsv_file. So when you run your commands, you must provide the path to the TSV file:
    commands = python manage.py import_name_basics path/to/name.basics.tsv
    The value path/to/name.basics.tsv gets passed into the commands and can be accessed using: file_path = options['tsv_file']
    """

    def handle(self, *args, **options):
        file_path = options['tsv_file']
        batch = []  # Temporary storage for model instances
        batch_size = 1000  # Will push records in db in batches not one by one

        def parse_int(value):  # for safe string to integer conversion, if value not digit return null
            return int(value) if value.isdigit() else None

        with open(file_path, encoding='utf-8') as tsvfile:
            reader = csv.DictReader(tsvfile,
                                    delimiter='\t')  # built-in Python class that reads tabular data and converts each row into a dictionary, using the first row as column headers.
            # \t means tab - our file has delimiter as tab

            for row in reader:
                person = Person(imdb_id=row['nconst'],
                                person_name=row['primaryName'],
                                birth_year=parse_int(row['birthYear']),
                                death_year=parse_int(row['deathYear']),
                                primary_profession=row['primaryProfession'],
                                known_for_title=row['knownForTitles']
                                )
                batch.append(person)

                if len(batch) >= batch_size:
                    Person.objects.bulk_create(batch,
                                               ignore_conflicts=True)  # This is the Django ORM method that inserts multiple model instances into the database in one efficient query.
                    # ignore_conflicts=True  | If a row already exists (e.g. same primary key or unique field), just skip it — don’t crash.
                    batch.clear()

                if batch:
                    Person.objects.bulk_create(batch, ignore_conflicts=True)

        self.stdout.write(self.style.SUCCESS("import complete"))
        # This is Django’s built-in way to print messages from a management commands to the terminal. We can also add colouring also checkout for more
