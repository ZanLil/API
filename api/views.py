from rest_framework import generics

from api.models import PerevalAdded
from api.serializers import PerevalAddedSerializer


class SubmitDataView(generics.CreateAPIView):
    """Класс-представления создания объекта pereval_added через API."""
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer
