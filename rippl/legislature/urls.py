from django.conf.urls import url

from . import views as v
from . import api

urlpatterns = [
    url(r'^reps/?$', v.RepresentativeList.as_view(), name='reps'),
    url(r'^reps/(?P<pk>\d+)/?$', v.RepresentativeDetail.as_view(), name='rep'),
    url(r'^reps/district/(?P<district_id>\d+)/?$', api.fetch_representative),
    url(r'^reps/contact/?$', api.fetch_address_reps),
    url(r'^district/?$', api.find_district, name='find_district'),
    url(r'^district/(?P<district_id>\d+)/?$', api.fetch_district),
]
