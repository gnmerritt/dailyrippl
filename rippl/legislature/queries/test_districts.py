from django.test import TestCase

from legislature.models import District, State
from . import districts


def maine():
    maine = State()
    maine.name = 'Maine'
    maine.abbr = 'ME'
    maine.id = 22
    return maine


class StateSerializerTest(TestCase):
    def test_state(self):
        state = maine()
        data = districts.StateSerializer(state).data

        self.assertIn('id', data)
        self.assertIn('name', data)
        self.assertEquals(data['name'], 'Maine')
        self.assertIn('abbr', data)
        self.assertEquals(data['abbr'], 'ME')


class DistrictSerializerTest(TestCase):
    def test_district(self):
        district = District()
        district.state = maine()
        district.number = 1
        district.id = 9
        data = districts.DistrictSerializer(district).data

        self.assertIn('id', data)
        self.assertIn('state', data)
        self.assertEquals(data['state'],
                          districts.StateSerializer(maine()).data)
        self.assertIn('number', data)
        self.assertEquals(data['number'], 1)
