from rest_framework import serializers
from timesheet.models import TimeSheetReport


class TimeSheetReportSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(read_only=True)
    client = serializers.PrimaryKeyRelatedField(read_only=True)
    date = serializers.DateField(read_only=True)

    class Meta:
        model = TimeSheetReport
        fields = '__all__'
