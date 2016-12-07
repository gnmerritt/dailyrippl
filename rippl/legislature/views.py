from django.views.generic import ListView, DetailView
from . import models


class RepresentativeList(ListView):
    context_object_name = 'reps'
    template_name = "legislature/representative_list.html"

    def get_queryset(self):
        return models.ActiveTerm.objects \
            .select_related() \
            .order_by('-term__chamber')


class RepresentativeDetail(DetailView):
    model = models.Representative
    context_object_name = 'rep'

    def get_context_data(self, **kwargs):
        context = super(RepresentativeDetail, self).get_context_data(**kwargs)
        context['terms'] = models.Term.objects.filter(rep=kwargs['object'])
        return context
