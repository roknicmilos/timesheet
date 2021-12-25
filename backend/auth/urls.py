from django.urls import path, include
from rest_framework.routers import DefaultRouter
from auth.views.user_view_set import UserViewSet
from auth.views.password_change_api_view import PasswordChangeAPIView
from auth.views.login_api_view import LoginAPIView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path(r'', include(router.urls)),
    path('users/<int:pk>/password-change/', PasswordChangeAPIView.as_view(), name='password-change'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
