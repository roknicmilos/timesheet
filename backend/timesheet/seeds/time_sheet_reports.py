from auth.models import User
from timesheet.models import TimeSheetReport

employee = User.objects.get(username='frodo')

seed_items = []

time_sheet_report_id = 1
for index, daily_time_sheet in enumerate(employee.daily_time_sheets.all()[:100]):
    if index % 5:
        # Create a single Time Sheet Report for the given employee and daily time sheet:
        time_sheet_report = TimeSheetReport(
            pk=time_sheet_report_id,
            hours=8,
            overtime_hours=0,
            daily_time_sheet=daily_time_sheet
        )
        time_sheet_report_id += 1
        seed_items.append(time_sheet_report)
        continue

    # Create two Time Sheet Reports for the given employee and daily time sheet:
    first_time_sheet_report = TimeSheetReport(
        pk=time_sheet_report_id,
        hours=6,
        overtime_hours=0,
        daily_time_sheet=daily_time_sheet
    )
    time_sheet_report_id += 1

    second_time_sheet_report = TimeSheetReport(
        pk=time_sheet_report_id,
        hours=2,
        overtime_hours=0,
        daily_time_sheet=daily_time_sheet
    )
    time_sheet_report_id += 1

    seed_items.extend([
        first_time_sheet_report,
        second_time_sheet_report,
    ])
