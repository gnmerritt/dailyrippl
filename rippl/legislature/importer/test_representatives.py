import datetime
from django.test import TestCase

from legislature.models import State, District, Representative, Term
from . import representatives


class RepImportTest(TestCase):
    loader = representatives.RepresentativeImport()
    loader.load_data("rippl/legislature/data/reps-sample.yml")

    def test_load_data(self):
        self.assertIn("Sherrod Brown", str(self.loader.data))
        self.assertEquals(2, len(self.loader.data))

    def test_db_import(self):
        self.assertEquals(0, Representative.objects.count())
        self.assertEquals(0, Term.objects.count())
        self.assertEquals(0, District.objects.count())

        self.loader.build()
        self.counts_after_load()
        # repeated loads of same data have no effect
        self.loader.build()
        self.counts_after_load()

        brown = Representative.objects.filter(bioguide_id='B000944').first()
        self.assertEquals("Sherrod", brown.first)
        self.assertEquals("Brown", brown.last)
        self.assertEquals("M", brown.gender)
        self.assertEquals(datetime.date(1952, 11, 9), brown.birthday)
        self.assertEquals("Lutheran", brown.religion)
        self.assertEquals("Sherrod Brown", brown.wikipedia_id)
        self.assertEquals("kg:/m/034s80", brown.google_id)

        oh_terms = Term.objects.filter(district__state__abbr='OH')
        self.assertEquals(3, oh_terms.count())
        self.assertEquals(1, len([t for t in oh_terms if t.is_active()]))

    def counts_after_load(self):
        self.assertEquals(2, Representative.objects.count())
        self.assertEquals(2, State.objects.count())
        self.assertEquals(6, Term.objects.count())
        self.assertEquals(3, District.objects.count())
