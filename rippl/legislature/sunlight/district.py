import requests

from rippl.settings import SUNLIGHT_KEY

from legislature.models import State, District


class DistrictMatcher(object):
    URL = 'https://congress.api.sunlightfoundation.com/districts/locate'

    def get_headers(self):
        headers = {}
        if SUNLIGHT_KEY is not None:
            headers['X-APIKEY'] = SUNLIGHT_KEY
        return headers

    def make_call(self, latitude, longitude):
        headers = self.get_headers()
        params = {
            'latitude': latitude,
            'longitude': longitude
        }
        results = requests.get(self.URL, params=params, headers=headers).json()
        if results.get('count', None) != 1:
            raise Exception('Bad response from sunlight: "{}"'.format(results))
        return results.get('results')[0]

    def find_district(self, latitude, longitude):
        state_district = self.make_call(latitude, longitude)
        state = state_district.get('state', None)
        db_state = State.objects.get(abbr=state)
        district = state_district.get('district', None)
        db_district = District.objects.get(state=db_state, number=district)
        return db_district
