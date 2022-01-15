from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.views import ClientViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='clients')
# TODO: implement nested router for Client's Project

urlpatterns = [
    path(r'', include(router.urls)),
]
