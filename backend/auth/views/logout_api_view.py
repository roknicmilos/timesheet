from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


class LogoutAPIView(APIView):

    @staticmethod
    def get(request, **kwargs) -> Response:
        Token.objects.get(user_id=request.user.pk).delete()
        return Response(status=200)
