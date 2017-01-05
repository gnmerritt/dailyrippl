from rest_framework import viewsets, serializers

from questing.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.exclude(name__exact='')
    serializer_class = TopicSerializer
