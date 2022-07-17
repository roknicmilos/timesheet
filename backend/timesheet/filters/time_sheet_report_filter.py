from django_filters import NumberFilter, DateFilter
from django_filters.rest_framework import FilterSet
from timesheet.filters import HasOvertimeBooleanField
from timesheet.models import TimeSheetReport


class TimeSheetReportFilter(FilterSet):
    employee_id = NumberFilter(field_name='daily_time_sheet__employee', lookup_expr='pk')
    project_id = NumberFilter(field_name='project', lookup_expr='pk')
    client_id = NumberFilter(field_name='project__client', lookup_expr='pk')
    category_id = NumberFilter(field_name='category', lookup_expr='pk')
    from_date = DateFilter(field_name='daily_time_sheet__date', lookup_expr='gte', label='from')
    until_date = DateFilter(field_name='daily_time_sheet__date', lookup_expr='lte', label='until')
    has_overtime = HasOvertimeBooleanField(field_name='overtime_hours')

    class Meta:
        model = TimeSheetReport
        fields = [
            'daily_time_sheet__employee',
            'project',
            'project__client',
            'category',
            'daily_time_sheet__date',
            'overtime_hours',
        ]
