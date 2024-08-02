from rest_framework import serializers

from read_api.models import ReadData


class ReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadData
        fields = '__all__'
