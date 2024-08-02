from rest_framework import serializers

from discussion_api.models import DiscussionData


class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionData
        fields = '__all__'
