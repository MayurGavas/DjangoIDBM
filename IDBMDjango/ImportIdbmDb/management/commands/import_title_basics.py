from django.core.management.base import BaseCommand
import csv
from ...models import Title

class Command(BaseCommand):
    help= 'Import Data from titles.basics'

    def add_arguments(self, parser):
        parser.add_argument('tsv_file',type=str)

    def handle(self, *args, **options):
        file_path= options['tsv_file']
        batch = []
        batch_size = 20000

        with open(file_path,encoding='utf-8') as tsvfile:
            reader = csv.DictReader(tsvfile,
                                    delimiter='\t')

            def parse_int(value):
                return int(value) if value.isdigit() else None

            for row in reader:
                title = Title(
                    tconst= row['tconst'],
                titleType = row['titleType'],
                primaryTitle = row['primaryTitle'],
                originalTitle = row['originalTitle'],
                isAdult = (row['isAdult']==1) ,
                startYear = parse_int(row['startYear']) if row['startYear'] != '\\N' else None,
                endYear = parse_int(row['endYear']) if row['endYear'] != '\\N' else None,
                runtimeMinutes = parse_int(row['runtimeMinutes']) if row['runtimeMinutes'] != '\\N' else None,
                genres = row['genres'] if row['genres'] != '\\N' else None
                )
                batch.append(title)

                if len(batch) >= batch_size:
                    Title.objects.bulk_create(batch,ignore_conflicts=True)
                    batch.clear()
                    self.stdout.write(self.style.SUCCESS("✅ 1 batch of 20000 title.basics.tsv import complete"))

        if batch:
            Title.objects.bulk_create(batch, ignore_conflicts=True)

        self.stdout.write(self.style.SUCCESS("✅ title.basics.tsv import complete"))


