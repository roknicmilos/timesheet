from django.db.models import Q
from django.http import JsonResponse
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from core.models import DailyTimeSheet, TimeSheetReport, User


class TimeSheetReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSheetReport
        fields = '__all__'


class DailyTimeSheetSerializer(serializers.ModelSerializer):
    time_sheet_reports = TimeSheetReportSerializer(many=True, read_only=True)

    class Meta:
        model = DailyTimeSheet
        fields = '__all__'


class DailyTimeSheetViewSet(viewsets.ViewSet):
    user: User = None

    def dispatch(self, request, *args, user_pk=None, **kwargs):
        try:
            self.user = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            return JsonResponse(data={'detail': 'User not found.'}, status=404)

        return super(DailyTimeSheetViewSet, self).dispatch(request, *args, user_pk=user_pk, **kwargs)

    def list(self, request, **kwargs):
        daily_time_sheets = DailyTimeSheet.objects.filter(self._get_list_filters(request=request))
        serializer = DailyTimeSheetSerializer(daily_time_sheets, many=True)
        return Response(data=serializer.data)

    def _get_list_filters(self, request) -> Q:
        filters = Q(employee=self.user)
        if 'from' in request.query_params:
            filters &= Q(date__gte=request.query_params.get('from'))
        if 'until' in request.query_params:
            filters &= Q(date__lte=request.query_params.get('until'))
        return filters

    def create(self, request, **kwargs):
        serializer = DailyTimeSheetSerializer(data={**request.data, 'employee': self.user.pk})
        if serializer.is_valid():
            daily_time_sheet = serializer.save()
            serializer = DailyTimeSheetSerializer(daily_time_sheet)
            return Response(data=serializer.data, status=201)
        return Response(data={'errors': serializer.errors}, status=400)


    def retrieve(self, request, pk=None, **kwargs):
        daily_time_sheets = get_object_or_404(DailyTimeSheet, pk=pk, employee=self.user)
        serializer = DailyTimeSheetSerializer(daily_time_sheets)
        return Response(data=serializer.data)

    def partial_update(self, request, pk=None, **kwargs):
        daily_time_sheet = get_object_or_404(DailyTimeSheet, pk=pk, employee=self.user)
        data = self._prepare_time_sheet_reports_data(request=request, daily_time_sheet_id=pk)
        daily_time_sheet_serializer = TimeSheetReportSerializer(data=data, many=True)
        if daily_time_sheet_serializer.is_valid():
            daily_time_sheet.time_sheet_reports.all().delete()
            daily_time_sheet_serializer.save()
            serializer = DailyTimeSheetSerializer(daily_time_sheet)
            return Response(data=serializer.data, status=200)
        return Response(data={'errors': daily_time_sheet_serializer.errors}, status=400)

    @staticmethod
    def _prepare_time_sheet_reports_data(request, daily_time_sheet_id: int) -> dict:
        data = request.data.get('time_sheet_reports', [])
        for item in data:
            item['daily_time_sheet'] = daily_time_sheet_id
        return data

    def destroy(self, request, pk=None, **kwargs):
        daily_time_sheet = get_object_or_404(DailyTimeSheet, pk=pk, employee=self.user)
        daily_time_sheet.delete()
        return Response(status=204)
