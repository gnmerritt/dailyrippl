from django.test import TestCase
from httmock import all_requests, response, HTTMock

from legislature.models import State, District
from .district import DistrictMatcher

STATE = {'state': 'MA', 'district': 7}
EXPECTED_RESPONSE = {
    'count': 1,
    'results': [STATE],
}


@all_requests
def sunlight_mock(url, request):
    if 'latitude=10' not in url.query:
        raise Exception("Wrong latitude: '{}'".format(url))
    if 'longitude=-10' not in url.query:
        raise Exception("Wrong longitude: '{}'".format(url))
    header = {'content-type': 'application/json'}
    return response(200, EXPECTED_RESPONSE, header, None, 5, request)


class DistrictMatcherTest(TestCase):
    def test_make_api_call(self):
        with HTTMock(sunlight_mock):
            matcher = DistrictMatcher()
            response = matcher.make_call(10, -10)
            self.assertEquals(response, STATE)

    def fake_call(self, lat, lng):
        self.assertEquals(lat, 10)
        self.assertEquals(lng, -10)
        return STATE

    def test_resp_to_db(self):
        matcher = DistrictMatcher()
        matcher.make_call = self.fake_call
        MA, _ = State.objects.get_or_create(**{
            'name': 'Massachusetts', 'abbr': 'MA'
        })
        expected_district, _ = District.objects.get_or_create(**{
            'state': MA, 'number': 7
        })

        d = matcher.find_district(10, -10)

        self.assertEquals(d, expected_district)

    def test_missing_district(self):
        matcher = DistrictMatcher()
        matcher.make_call = self.fake_call
        MA, _ = State.objects.get_or_create(**{
            'name': 'Massachusetts', 'abbr': 'MA'
        })

        with self.assertRaises(District.DoesNotExist):
            matcher.find_district(10, -10)

    def test_missing_state(self):
        matcher = DistrictMatcher()
        matcher.make_call = self.fake_call

        with self.assertRaises(State.DoesNotExist):
            matcher.find_district(10, -10)
