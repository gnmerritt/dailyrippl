import json
from legislature.models import State


class StateImporter(object):
    STATES = "rippl/legislature/data/us_states.json"

    def __init__(self):
        self.json = self.load_json()

    def load_json(self):
        with open(self.STATES, 'r') as json_file:
            return json.load(json_file)

    def build(self):
        for abbr, name in self.json.items():
            State.objects.get_or_create(abbr=abbr, name=name)
