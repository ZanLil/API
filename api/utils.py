from rest_framework import serializers


def check_required_keys(dictionary, required_keys, error_message, field=''):
    """Дополнительная функция для перебора ключей и их валидации."""
    for key in required_keys:
        if key not in dictionary:
            raise serializers.ValidationError(error_message.format(field, key))
