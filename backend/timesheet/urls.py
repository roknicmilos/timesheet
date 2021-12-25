from django.urls import path, include
from rest_framework_nested.routers import NestedSimpleRouter
from timesheet.views.daily_time_sheet_view_set import DailyTimeSheetViewSet
from auth.urls import router as auth_router

daily_time_sheets_router = NestedSimpleRouter(auth_router, r'users', lookup='user')
daily_time_sheets_router.register(r'daily-time-sheets', DailyTimeSheetViewSet, basename='daily-time-sheets')

urlpatterns = [
    path(r'', include(daily_time_sheets_router.urls)),
]
