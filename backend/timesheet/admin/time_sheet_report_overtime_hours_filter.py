from django.contrib.admin import SimpleListFilter
from django.db.models import QuerySet
from timesheet.models import TimeSheetReport


class TimeSheetReportOvertimeHoursFilter(SimpleListFilter):
    title = 'has overtime'
    parameter_name = 'has_overtime'
    LOOKUP_KEY_TRUE = '1'
    LOOKUP_KEY_FALSE = '2'

    def lookups(self, request, model_admin):
        return [
            (self.LOOKUP_KEY_TRUE, 'Yes'),
            (self.LOOKUP_KEY_FALSE, 'No'),
        ]

    def queryset(self, request, queryset: QuerySet):
        has_overtime = self.value()
        if has_overtime == self.LOOKUP_KEY_TRUE:
            return TimeSheetReport.objects.filter(overtime_hours__gt=0)
        if has_overtime == self.LOOKUP_KEY_FALSE:
            return TimeSheetReport.objects.filter(overtime_hours=0)
        return queryset
