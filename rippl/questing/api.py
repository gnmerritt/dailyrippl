from rest_framework import viewsets, serializers

from questing.models import Topic
from rippl.throttling import BurstRateThrottle, SustainedRateThrottle


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class TopicViewSet(viewsets.ModelViewSet):
    throttle_classes = (BurstRateThrottle, SustainedRateThrottle)
    queryset = Topic.objects.exclude(name__exact='')
    serializer_class = TopicSerializer
