from django.conf.urls import url

from . import views as v

urlpatterns = [
    url(r'^reps/?$', v.RepresentativeList.as_view()),
    url(r'^reps/(?P<pk>\d+)/?$', v.RepresentativeDetail.as_view(), name='rep'),
]
