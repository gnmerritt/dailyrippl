from django.core.management.base import BaseCommand

from legislature.importer.states import StateImporter
from legislature.importer.representatives import RepresentativeImport
from legislature.importer.active_terms import ActiveTermMaterialize
from legislature.models import Representative, ActiveTerm


class Command(BaseCommand):
    help = 'Imports representatives, terms and districts from a data file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def success(self, line):
        self.stdout.write(self.style.SUCCESS(line))

    def handle(self, *args, **options):
        self.stdout.write("Importing US states")
        StateImporter().build()
        self.success("states imported")
        filename = options['filename']
        self.stdout.write("Importing data from '%s'" % filename)
        importer = RepresentativeImport()
        importer.load_data(filename)
        self.success("loaded data")
        importer.build()
        self.success("representative import succeeded")
        self.success("DB contains %d reps" % Representative.objects.count())
        terms = ActiveTermMaterialize()
        terms.build()
        self.success("Found %d active terms" % ActiveTerm.objects.count())
