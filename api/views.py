from rest_framework.views import APIView
from rest_framework.response import Response


class SubmitDataView(APIView):

    def post(self, request):
        return Response({'status': 200})
