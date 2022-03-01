from django.db.models import Q
from rest_framework.response import Response
from rest_framework import viewsets
from main.utils import get_bool_url_param_value, Paginator
from timesheet.models import TimeSheetReport
from timesheet.serializers import TimeSheetReportSerializer


class TimeSheetReportViewSet(viewsets.ViewSet):

    def list(self, request, **kwargs):
        filters = self._get_list_filters(url_params=request.query_params)
        queryset = TimeSheetReport.objects.filter(filters)
        paginator = Paginator(queryset=queryset, request=request)
        serializer = TimeSheetReportSerializer(paginator.page, many=True)
        return Response(data=serializer.data)

    @staticmethod
    def _get_list_filters(url_params: dict) -> Q:
        filters = Q()

        if 'employee_id' in url_params:
            filters &= Q(daily_time_sheet__employee__pk=url_params.get('employee_id'))
        if 'project_id' in url_params:
            filters &= Q(project__pk=url_params.get('project_id'))
        if 'client_id' in url_params:
            filters &= Q(project__client__pk=url_params.get('client_id'))
        if 'category_id' in url_params:
            filters &= Q(category__pk=url_params.get('category_id'))
        if 'from' in url_params:
            filters &= Q(date__gte=url_params.get('from'))
        if 'until' in url_params:
            filters &= Q(date__lte=url_params.get('until'))

        has_overtime = get_bool_url_param_value(url_params=url_params, param_name='has_overtime')
        if has_overtime is True:
            filters &= Q(overtime_hours__gt=0)
        elif has_overtime is False:
            filters &= Q(overtime_hours=0)

        return filters
