from django.test import TestCase

from legislature.models import State
from . import states

NUM_STATES = 59


class StateImporterTest(TestCase):
    loader = states.StateImporter()

    def test_json_load(self):
        self.assertEquals(NUM_STATES, len(self.loader.json))

    def test_db_load(self):
        self.assertEquals(0, State.objects.count())
        self.loader.build()
        self.assertEquals(NUM_STATES, State.objects.count())
        # doesn't cause problems if you run it again
        self.loader.build()
        self.assertEquals(NUM_STATES, State.objects.count())

        ma = State.objects.filter(abbr='MA').first()
        self.assertEquals(ma.name, 'Massachusetts')
