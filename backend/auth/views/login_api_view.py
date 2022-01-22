from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from auth.serializers import LoginSerializer


class LoginAPIView(APIView):

    @staticmethod
    def post(request, **kwargs) -> Response:
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            token, _ = Token.objects.get_or_create(user=serializer.user)
            return Response(data={'token': token.key}, status=200)
        return Response(data={'errors': serializer.errors}, status=400)
