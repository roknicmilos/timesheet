from datetime import timedelta
from django.utils import timezone
from auth.models import User
from timesheet.models import DailyTimeSheet

employee = User.objects.get(username='frodo')

current_year_first_date = timezone.now().replace(month=1, day=1)
current_year_last_date = current_year_first_date.replace(year=current_year_first_date.year + 1) - timedelta(days=1)

seed_items = []

daily_time_sheet_date = current_year_first_date
daily_time_sheet_id = 1
while daily_time_sheet_date < current_year_last_date:
    daily_time_sheet = DailyTimeSheet(
        pk=daily_time_sheet_id,
        employee=employee,
        date=daily_time_sheet_date.date()
    )
    seed_items.append(daily_time_sheet)
    daily_time_sheet_date += timedelta(days=1)
    daily_time_sheet_id += 1
