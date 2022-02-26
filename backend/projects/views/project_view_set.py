from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from auth.authentication import TokenAuthentication
from auth.permissions import IsAdmin
from main.utils import paginate_queryset
from main.viewsets import ViewSet
from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectViewSet(ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]
    model_class = Project
    available_alphabet_letters_default_field = 'name'

    def list(self, request, **kwargs):
        projects = paginate_queryset(queryset=self.model_class.objects.all(), request=request)
        serializer = ProjectSerializer(projects, many=True)
        return Response(data=serializer.data)


    def create(self, request, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = self.model_class.objects.create(**serializer.validated_data)
            serializer = ProjectSerializer(project)
            return Response(data=serializer.data, status=201)
        return Response(data={'errors': serializer.errors}, status=400)

    def update(self, request, pk=None) -> Response:
        project = get_object_or_404(self.model_class, pk=pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            project.update(**serializer.validated_data)
            serializer = ProjectSerializer(project)
            return Response(data=serializer.data, status=200)
        return Response(data={'errors': serializer.errors}, status=400)

    def destroy(self, request, pk=None) -> Response:
        project = get_object_or_404(self.model_class, pk=pk)
        project.delete()
        return Response(status=204)
