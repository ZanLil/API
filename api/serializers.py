from rest_framework import serializers

from .models import PerevalAdded
from .utils import check_required_keys


class PerevalAddedSerializer(serializers.ModelSerializer):
    """Serializer для модели PerevalAdded."""
    raw_data = serializers.JSONField(required=True)
    images = serializers.JSONField(required=True)

    class Meta:
        model = PerevalAdded
        fields = ['raw_data', 'images']

    def validate_raw_data(self, value):
        """Валидация поля raw_data."""
        if not value:
            raise serializers.ValidationError("raw_data не может быть пустым")
        if not isinstance(value, dict):
            raise serializers.ValidationError("значением raw_data должно быть {}")
        required_keys = ['beautyTitle', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'level']
        error_message = "raw_data{} должен содержать ключ '{}'."
        check_required_keys(value, required_keys, error_message)
        for field, keys in [('user', ['email', 'phone', 'fam', 'name', 'otc']),
                            ('coords', ['latitude', 'longitude', 'height']),
                            ('level', ['winter', 'summer', 'autumn', 'spring'])]:
            check_required_keys(value.get(field, {}), keys, error_message, f'.{field}')
        return value

    def validate_images(self, value):
        """Валидация поля images."""
        if not value:
            raise serializers.ValidationError("images не может быть пустым")
        if not isinstance(value, list):
            raise serializers.ValidationError("значением images должно быть []")
        for item in value:
            if 'id' not in item or 'title' not in item:
                raise serializers.ValidationError("объекты images должны содержать ключи 'id' и 'title'.")
        return value


class PerevalAddedAllFieldsSerializer(serializers.ModelSerializer):
    """Serializer для модели PerevalAdded со всеми полями."""

    class Meta:
        model = PerevalAdded
        fields = '__all__'


class PerevalUpdateSerializer(serializers.ModelSerializer):
    """Serializer для модели PerevalAdded с исключением некоторых полей."""

    class Meta:
        model = PerevalAdded
        exclude = ['status']

    def validate_raw_data(self, value):
        """Валидация поля raw_data."""
        instance_user_data = self.instance.raw_data.get('user')
        value_user_data = value.get('user')
        keys = ['fam', 'name', 'otc', 'email', 'phone']
        for key in keys:
            if instance_user_data.get(key) != value_user_data.get(key):
                raise serializers.ValidationError({'state': 0, 'message': f"Нельзя изменять поле '{key}'."})
        return value
