from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from core.views.user_view_set import UserViewSet
from core.views.daily_time_sheet_view_set import DailyTimeSheetViewSet
from core.views.password_change_api_view import PasswordChangeAPIView
from core.views.login_api_view import LoginAPIView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

daily_time_sheets_router = NestedSimpleRouter(router, r'users', lookup='user')
daily_time_sheets_router.register(r'daily-time-sheets', DailyTimeSheetViewSet, basename='daily-time-sheets')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(daily_time_sheets_router.urls)),
    path('users/<int:pk>/password-change/', PasswordChangeAPIView.as_view(), name='password-change'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
