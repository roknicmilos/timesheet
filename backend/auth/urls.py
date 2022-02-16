from django.urls import path, include
from rest_framework.routers import DefaultRouter
from auth.views import (
    UserViewSet,
    PasswordChangeAPIView,
    LoginAPIView,
    LogoutAPIView
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path(r'', include(router.urls)),
    path('users/<int:pk>/password-change/', PasswordChangeAPIView.as_view(), name='password-change'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]
