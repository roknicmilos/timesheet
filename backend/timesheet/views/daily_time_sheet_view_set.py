from django.db.models import Q
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from auth.authentication import TokenAuthentication
from auth.permissions import HasAccessToUserResources
from main.utils import Paginator
from timesheet.models import DailyTimeSheet, TimeSheetReport
from timesheet.serializers import DailyTimeSheetSerializer


class DailyTimeSheetViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, HasAccessToUserResources]

    def list(self, request, **kwargs):
        filters = self._get_list_filters(url_params=request.query_params)
        queryset = DailyTimeSheet.objects.filter(filters)
        paginator = Paginator(queryset=queryset, request=request)
        serializer = DailyTimeSheetSerializer(paginator.page, many=True)
        return Response(data=serializer.data)

    def _get_list_filters(self, url_params: dict) -> Q:
        filters = Q(employee=self.request.user)
        if 'from' in url_params:
            filters &= Q(date__gte=url_params.get('from'))
        if 'until' in url_params:
            filters &= Q(date__lte=url_params.get('until'))
        return filters

    def create(self, request, **kwargs):
        serializer = DailyTimeSheetSerializer(data={**request.data, 'employee': self.request.user.pk})
        if serializer.is_valid():
            daily_time_sheet = DailyTimeSheet.objects.create(**serializer.validated_data)
            serializer = DailyTimeSheetSerializer(daily_time_sheet)
            return Response(data=serializer.data, status=201)
        return Response(data={'errors': serializer.errors}, status=400)

    def retrieve(self, request, pk=None, **kwargs):
        daily_time_sheets = get_object_or_404(DailyTimeSheet, pk=pk, employee=self.request.user)
        serializer = DailyTimeSheetSerializer(daily_time_sheets)
        return Response(data=serializer.data)

    def partial_update(self, request, pk=None, **kwargs):
        daily_time_sheet = get_object_or_404(DailyTimeSheet, pk=pk, employee=self.request.user)
        data = self._prepare_time_sheet_reports_data(request=request, daily_time_sheet_id=pk)
        time_sheet_report_serializer = DailyTimeSheetSerializer.TimeSheetReportSerializer(data=data, many=True)
        if time_sheet_report_serializer.is_valid():
            daily_time_sheet.time_sheet_reports.all().delete()
            TimeSheetReport.objects.create_batch(*time_sheet_report_serializer.validated_data)
            serializer = DailyTimeSheetSerializer(daily_time_sheet)
            return Response(data=serializer.data, status=200)
        return Response(data={'errors': time_sheet_report_serializer.errors}, status=400)

    @staticmethod
    def _prepare_time_sheet_reports_data(request, daily_time_sheet_id: int) -> dict:
        data = request.data.get('time_sheet_reports', [])
        for item in data:
            item['daily_time_sheet'] = daily_time_sheet_id
        return data

    def destroy(self, request, pk=None, **kwargs):
        daily_time_sheet = get_object_or_404(DailyTimeSheet, pk=pk, employee=self.request.user)
        daily_time_sheet.delete()
        return Response(status=204)
