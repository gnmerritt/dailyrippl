from rest_framework import viewsets, serializers

from questing.models import Topic
from rippl.throttling import BurstRateThrottle, SustainedRateThrottle


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class TopicViewSet(viewsets.ModelViewSet):
    throttle_classes = (BurstRateThrottle, SustainedRateThrottle)
    serializer_class = TopicSerializer

    def get_queryset(self):
        queryset = Topic.objects.exclude(name__exact='')
        search = self.request.query_params.get('q', None)
        if search is not None:
            queryset = queryset.filter(name__icontains=search)
        return queryset
