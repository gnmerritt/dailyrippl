from rest_framework import viewsets, serializers

from bills.models import Bill


class SponsorRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return '%s %s' % (value.first, value.last)


class BillSerializer(serializers.ModelSerializer):

    topics = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='name')
    sponsor = SponsorRelatedField(read_only=True)

    class Meta:
        model = Bill
        fields = '__all__'


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects \
        .exclude(official_title__isnull=True) \
        .exclude(official_title__exact='')
    serializer_class = BillSerializer
