from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.views import ClientViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'projects', ProjectViewSet, basename='projects')
# TODO: implement nested router for Client's Project

urlpatterns = [
    path(r'', include(router.urls)),
]
