from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.views import ClientViewSet, ProjectViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'categories', CategoryViewSet, basename='categories')
# TODO: implement nested router for Client's Project

urlpatterns = [
    path(r'', include(router.urls)),
]
