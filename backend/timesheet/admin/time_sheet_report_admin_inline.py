from django.contrib import admin
from timesheet.models import TimeSheetReport


class TimeSheetReportAdminInline(admin.TabularInline):
    model = TimeSheetReport
    extra = 0
