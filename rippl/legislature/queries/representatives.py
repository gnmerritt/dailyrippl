from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from legislature.models import ActiveTerm, Term, District, Representative


class RepresentativeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Representative
        fields = ('first', 'last', 'bioguide_id')


class RepresentativeFetcher(object):
    """Fetchers the active representatives in the house & senate for a given
    congressional district."""
    def fetch(self, district_id):
        self.district = get_object_or_404(District, pk=district_id)
        terms = ActiveTerm.objects \
            .filter(self.senate_filter() | self.house_filter()) \
            .select_related() \
            .all()
        return self.extract_chambers(terms)

    def senate_filter(self):
        return Q(term__district__state__id=self.district.state_id,
                 term__chamber=Term.SENATE)

    def house_filter(self):
        return Q(term__district__id=self.district.id, term__chamber=Term.HOUSE)

    def extract_chambers(self, terms):
        return {
            chamber: [RepresentativeSerializer(t.rep).data
                      for t in terms if t.term.chamber == chamber]
            for chamber in [Term.HOUSE, Term.SENATE]
        }
