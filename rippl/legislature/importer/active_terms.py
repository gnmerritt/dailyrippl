import datetime
from legislature.models import ActiveTerm, Term


class ActiveTermMaterialize(object):
    """Creates ActiveTerm records to join reps to their active term"""
    def build(self):
        today = datetime.datetime.now().date()
        active_terms = Term.objects.filter(end__gte=today)
        for term in active_terms:
            ActiveTerm.objects.get_or_create(**{
                'rep': term.rep, 'term': term
            })
