from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from timesheet.views import DailyTimeSheetViewSet, TimeSheetReportViewSet
from auth.urls import router as auth_router

router = DefaultRouter()
router.register(r'time-sheet-reports', TimeSheetReportViewSet, basename='time-sheet-reports')

daily_time_sheets_router = NestedSimpleRouter(auth_router, r'users', lookup='user')
daily_time_sheets_router.register(r'daily-time-sheets', DailyTimeSheetViewSet, basename='daily-time-sheets')

urlpatterns = [
    path(r'', include(router.urls + daily_time_sheets_router.urls)),
]
