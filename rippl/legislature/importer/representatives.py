import yaml
from legislature.models import State, District, Representative, Term


class RepresentativeImport(object):
    """Importer for data from the unitedstates/congress-legislators repo"""
    def load_data(self, filename):
        self.file = filename
        with open(filename, 'r') as contents:
            self.data = yaml.load(contents)

    def build(self):
        for rep in self.data:
            db_rep = self.import_rep(rep)
            self.import_terms(db_rep, rep)

    def import_rep(self, rep):
        ids = rep.get('id', {})
        bioguide = ids.get('bioguide', None)
        if not bioguide:
            return
        db_rep = self.get_rep(bioguide)
        db_rep.google_id = ids.get('google_entity_id', None)
        db_rep.wikipedia_id = ids.get('wikipedia', None)

        name = rep.get('name', {})
        db_rep.first = name['first']
        db_rep.last = name['last']

        bio = rep.get('bio', {})
        db_rep.birthday = bio.get('birthday', None)
        db_rep.gender = bio.get('gender', 'M')
        db_rep.religion = bio.get('religion', None)

        db_rep.save()
        return db_rep

    def get_rep(self, bioguide_id):
        hits = Representative.objects.filter(bioguide_id=bioguide_id)
        if hits.count() > 0:
            return hits.first()
        rep = Representative()
        rep.bioguide_id = bioguide_id
        return rep

    def import_terms(self, db_rep, data):
        terms = data.get('terms', [])
        for term in terms:
            district = self.import_district(term)
            self.get_term(term, db_rep, district)

    def get_term(self, term, rep, district):
        body = Term.SENATE if term['type'] == 'sen' else Term.HOUSE
        start = term['start']
        end = term['end']
        party = term['party'][0]
        db_term, _ = Term.objects.get_or_create(**{
            'chamber': body, 'start': start, 'end': end, 'district': district,
            'party': party, 'rep': rep
        })
        return db_term

    def import_district(self, term):
        state, _ = State.objects.get_or_create(abbr=term['state'])
        district_num = term.get('district', -1)
        district, _ = District.objects.get_or_create(
            state=state, number=district_num
        )
        return district
