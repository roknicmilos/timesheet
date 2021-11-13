from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from core.views.user import UserViewSet
from core.views.daily_time_sheet import DailyTimeSheetViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

daily_time_sheets_router = NestedSimpleRouter(router, r'users', lookup='user')
daily_time_sheets_router.register(r'daily-time-sheets', DailyTimeSheetViewSet, basename='daily_time_sheets')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(daily_time_sheets_router.urls)),
]
