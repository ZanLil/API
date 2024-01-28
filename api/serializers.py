from rest_framework import serializers

from .models import PerevalAdded


class PerevalAddedSerializer(serializers.ModelSerializer):
    """Serializer для модели PerevalAdded."""
    raw_data = serializers.JSONField()
    images = serializers.JSONField()

    class Meta:
        model = PerevalAdded
        fields = ['raw_data', 'images']


class PerevalAddedAllFieldsSerializer(serializers.ModelSerializer):
    """Serializer для модели PerevalAdded со всеми полями."""

    class Meta:
        model = PerevalAdded
        fields = '__all__'


class PerevalUpdateSerializer(serializers.ModelSerializer):
    """Serializer для модели PerevalAdded с исключением некоторых полей."""

    class Meta:
        model = PerevalAdded
        exclude = ['status', 'user_email']
