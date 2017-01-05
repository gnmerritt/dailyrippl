from rest_framework import viewsets, serializers

from bills.models import Bill
from rippl.throttling import BurstRateThrottle, SustainedRateThrottle


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'


class BillViewSet(viewsets.ModelViewSet):
    throttle_classes = (BurstRateThrottle, SustainedRateThrottle)

    queryset = Bill.objects \
        .exclude(official_title__isnull=True) \
        .exclude(official_title__exact='')
    serializer_class = BillSerializer
