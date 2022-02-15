from rest_framework.response import Response
from rest_framework.views import APIView
from auth.serializers import LoginSerializer


class LoginAPIView(APIView):

    @staticmethod
    def post(request, **kwargs) -> Response:
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(data=serializer.validated_data, status=200)
        return Response(data={'errors': serializer.errors}, status=400)
