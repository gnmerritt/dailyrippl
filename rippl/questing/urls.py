from django.conf.urls import include, url
from rest_framework import routers

from questing import api

router = routers.DefaultRouter()
router.register(r'topics', api.TopicViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
