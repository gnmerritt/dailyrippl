from rest_framework import serializers

from legislature.models import District, State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = District
        fields = '__all__'
