from rest_framework.permissions import IsAuthenticated
from auth.authentication import TokenAuthentication
from auth.permissions import HasAccessToUserResources
from django_filters import rest_framework as filters
from main.viewsets import ViewSet
from timesheet.filters import TimeSheetReportFilter
from timesheet.models import TimeSheetReport
from timesheet.serializers import TimeSheetReportSerializer


class TimeSheetReportViewSet(ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, HasAccessToUserResources]
    model_class = TimeSheetReport
    serializer_class = TimeSheetReportSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TimeSheetReportFilter
