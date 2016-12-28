from django.conf.urls import url

from . import views as v
from . import api

urlpatterns = [
    url(r'^reps/?$', v.RepresentativeList.as_view(), name='reps'),
    url(r'^reps/(?P<pk>\d+)/?$', v.RepresentativeDetail.as_view(), name='rep'),

    url(r'^district/?$', api.find_district, name='find_district'),
]
