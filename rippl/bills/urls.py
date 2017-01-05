from django.conf.urls import include, url
from rest_framework import routers

from bills import api

router = routers.DefaultRouter()
router.register(r'bills', api.BillViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
