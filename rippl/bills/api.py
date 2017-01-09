from rest_framework import viewsets, serializers

from bills.models import Bill
from rippl.throttling import BurstRateThrottle, SustainedRateThrottle


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'


class BillViewSet(viewsets.ModelViewSet):
    throttle_classes = (BurstRateThrottle, SustainedRateThrottle)
    serializer_class = BillSerializer

    def get_queryset(self):
        queryset = Bill.objects \
            .exclude(official_title__isnull=True) \
            .exclude(official_title__exact='')
        topics = self.request.query_params.getlist('t')
        if topics:
            queryset = queryset.filter(topics__in=topics)
        return queryset
