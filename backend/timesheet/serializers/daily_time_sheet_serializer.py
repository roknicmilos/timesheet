from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from timesheet.models import DailyTimeSheet, TimeSheetReport


class TimeSheetReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSheetReport
        fields = '__all__'


class DailyTimeSheetSerializer(serializers.ModelSerializer):
    class TimeSheetReportSerializer(serializers.ModelSerializer):
        class Meta:
            model = TimeSheetReport
            fields = '__all__'

    time_sheet_reports = TimeSheetReportSerializer(many=True, read_only=True)

    class Meta:
        model = DailyTimeSheet
        fields = '__all__'

    def validate(self, attrs):
        attrs = super(DailyTimeSheetSerializer, self).validate(attrs)

        if DailyTimeSheet.objects.filter(date=attrs.get('date'), employee=attrs.get('employee')).exists():
            raise ValidationError('Daily time sheet with this user and date already exists')

        return attrs
