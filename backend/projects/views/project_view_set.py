from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import  viewsets
from auth.authentication import TokenAuthentication
from auth.permissions import IsAdmin
from main.utils import paginate_queryset
from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    def list(self, request, **kwargs):
        projects = paginate_queryset(queryset=Project.objects.all(), request=request)
        serializer = ProjectSerializer(projects, many=True)
        return Response(data=serializer.data)


    def create(self, request, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = Project.objects.create(**serializer.validated_data)
            serializer = ProjectSerializer(project)
            return Response(data=serializer.data, status=201)
        return Response(data={'errors': serializer.errors}, status=400)

    @staticmethod
    def update(request, pk=None) -> Response:
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            project.update(**serializer.validated_data)
            serializer = ProjectSerializer(project)
            return Response(data=serializer.data, status=200)
        return Response(data={'errors': serializer.errors}, status=400)

    @staticmethod
    def destroy(request, pk=None) -> Response:
        project = get_object_or_404(Project, pk=pk)
        project.delete()
        return Response(status=204)
