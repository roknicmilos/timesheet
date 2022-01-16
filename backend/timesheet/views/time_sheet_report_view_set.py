from django.db.models import Q
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from main.utils import paginate_queryset, get_bool_url_param_value
from timesheet.models import TimeSheetReport


class TimeSheetReportSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(read_only=True)
    client = serializers.PrimaryKeyRelatedField(read_only=True)
    date = serializers.DateField(read_only=True)

    class Meta:
        model = TimeSheetReport
        fields = '__all__'


class TimeSheetReportViewSet(viewsets.ViewSet):

    def list(self, request, **kwargs):
        filters = self._get_list_filters(url_params=request.query_params)
        time_sheet_reports = paginate_queryset(queryset=TimeSheetReport.objects.filter(filters), request=request)
        serializer = TimeSheetReportSerializer(time_sheet_reports, many=True)
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
