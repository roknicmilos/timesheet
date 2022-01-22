from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from auth.authentication import TokenAuthentication
from auth.models import User
from auth.permissions import HasAccessToUserResources
from auth.serializers import PasswordSerializer


class PasswordChangeAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, HasAccessToUserResources]

    @staticmethod
    def post(request, pk=None, **kwargs) -> Response:
        user = get_object_or_404(User, pk=pk)
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(raw_password=serializer.validated_data.get('password'))
            user.save()
            return Response(data={}, status=200)
        return Response(data={'errors': serializer.errors}, status=400)
