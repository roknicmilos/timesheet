from django.contrib import admin
from main.admin import ModelAdmin
from timesheet.admin.time_sheet_report_admin_inline import TimeSheetReportAdminInline
from timesheet.models import DailyTimeSheet


@admin.register(DailyTimeSheet)
class DailyTimeSheetAdmin(ModelAdmin):
    list_display = ('id', 'date', 'employee', 'time_sheet_report_count',)
    search_fields = ('employee__email', 'employee__name',)
    readonly_fields = ('id', 'time_sheet_report_count',)
    inlines = [
        TimeSheetReportAdminInline,
    ]

    def time_sheet_report_count(self, obj: DailyTimeSheet = None) -> int:
        return obj.time_sheet_reports.count() if obj else 0

    time_sheet_report_count.short_description = 'time sheet reports'
