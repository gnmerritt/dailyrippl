import datetime
from django.test import TestCase

from legislature.models import ActiveTerm
from . import representatives
from . import active_terms


class ActiveTermTest(TestCase):
    loader = representatives.RepresentativeImport()
    loader.load_data("rippl/legislature/data/reps-sample.yml")

    def test_active_term_materialize(self):
        self.loader.build()

        self.assertEquals(0, ActiveTerm.objects.count())
        importer = active_terms.ActiveTermMaterialize()
        importer.build()

        self.assertEquals(2, ActiveTerm.objects.count())
        terms = ActiveTerm.objects.select_related('term').select_related('rep')
        self.assertEquals(2, len(terms))
        sherrod = [t for t in terms if t.rep.first == "Sherrod"]
        self.assertEquals(1, len(sherrod))
        # this term isn't real - comes from the test yml file
        term = sherrod[0].term
        self.assertEquals('D', term.party)
        self.assertEqual('HOR', term.chamber)
        self.assertEqual(datetime.date(year=1997, month=1, day=7), term.start)
        self.assertEqual(datetime.date(year=2020, month=1, day=3), term.end)

        # make sure running again doesn't add more records
        importer.build()
        self.assertEquals(2, ActiveTerm.objects.count())
