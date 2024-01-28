from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import PerevalAdded
from api.serializers import PerevalAddedSerializer, PerevalAddedAllFieldsSerializer, PerevalUpdateSerializer


class SubmitDataView(APIView):
    """
    Класс-представление для создания объекта PerevalAdded и для получения записей,
    которые принадлежат определенному email.
    """

    @swagger_auto_schema(
        operation_summary='Получение записей по email',
        operation_description='Данный метод позволяет получить все записи,'
                              'которые сделал пользователь с определенным email',
        manual_parameters=[
            openapi.Parameter('user__email', in_=openapi.IN_QUERY, description='email пользователя',
                              type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request):
        """Логика для обработки GET-запроса."""
        user_email = request.query_params.get('user__email', None)
        if user_email:
            data = PerevalAdded.objects.filter(user_email=user_email).values()
            return Response({'status': status.HTTP_200_OK, 'data': data}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Укажите параметр user__email в запросе.'},
                status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Создание объекта',
        operation_description='Данный метод позволяет создавать новые записи',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'raw_data': openapi.Schema(type=openapi.TYPE_OBJECT),
                'images': openapi.Schema(type=openapi.TYPE_OBJECT),
            },
            required=['raw_data', 'images']
        ),
    )
    def post(self, request):
        """Логика для обработки POST-запроса."""
        user = self.request.user
        if not user.is_anonymous:
            user_email = user.email
            data = request.data.copy()
            data['user_email'] = user_email
            serializer = PerevalAddedSerializer(data=data)
        else:
            serializer = PerevalAddedSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class SubmitDataDetailView(APIView):
    """Класс-представление для работы с конкретным объектом PerevalAdded."""

    @swagger_auto_schema(
        operation_summary='Получение данных',
        operation_description='Данный метод позволяет получить все данные записи по id.',
    )
    def get(self, request, id):
        """Логика для обработки GET-запроса"""
        try:
            instance = PerevalAdded.objects.get(id=id)
            serializer = PerevalAddedAllFieldsSerializer(instance)
            return Response(serializer.data)
        except PerevalAdded.DoesNotExist:
            return Response({'status': status.HTTP_404_NOT_FOUND, "message": "Не найдено"},
                            status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Редактирование",
        operation_description="Данный метод позволяет редактировать существующие записи, которые имеют статус \"new\".",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'raw_data': openapi.Schema(type=openapi.TYPE_OBJECT),
                'images': openapi.Schema(type=openapi.TYPE_OBJECT),
            },
            required=['raw_data', 'images']
        ),
    )
    def patch(self, request, id):
        """Логика для обработки PATCH-запроса."""
        try:
            instance = PerevalAdded.objects.get(id=id)
            if instance.status != PerevalAdded.Status.NEW:
                return Response(
                    {"state": 0, "message": "Невозможно редактировать записи с статусом отличным от 'new'."},
                    status=status.HTTP_400_BAD_REQUEST)

            serializer = PerevalUpdateSerializer(instance, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({"state": 1}, status=status.HTTP_200_OK)
            return Response({"state": 0, "message": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)
        except PerevalAdded.DoesNotExist:
            return Response({'status': status.HTTP_404_NOT_FOUND, "message": "Не найдено"},
                            status=status.HTTP_404_NOT_FOUND)
