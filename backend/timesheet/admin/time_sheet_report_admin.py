from django.contrib import admin
from main.admin import ModelAdmin
from timesheet.admin.time_sheet_report_overtime_hours_filter import TimeSheetReportOvertimeHoursFilter
from timesheet.models import TimeSheetReport


@admin.register(TimeSheetReport)
class TimeSheetReportAdmin(ModelAdmin):
    list_display = ('id', 'date', 'employee', 'project', 'hours', 'overtime_hours',)
    list_filter = (
        'daily_time_sheet__date',
        TimeSheetReportOvertimeHoursFilter,
    )
    search_fields = (
        'project__name',
        'daily_time_sheet__employee__username',
        'daily_time_sheet__employee__email',
        'daily_time_sheet__employee__name',
    )
    fields = ('id', 'employee', 'daily_time_sheet', 'project', 'hours', 'overtime_hours', 'description',)
    readonly_fields = ('id',)
