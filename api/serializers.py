from rest_framework import serializers

from .models import PerevalAdded


class PerevalAddedSerializer(serializers.ModelSerializer):
    """Serializer для модели PerevalAdded."""

    class Meta:
        model = PerevalAdded
        fields = ['raw_data', 'images']
