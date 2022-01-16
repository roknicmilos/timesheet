from datetime import timedelta
from django.utils import timezone
from auth.models import User
from timesheet.models import DailyTimeSheet
from auth.seeds.users import seed_items as user_seeds


seed_items = []

# Create Daily Time Sheet for each day of the current year for
# the given employee and add it to the seed_items collection:
current_year_first_date = timezone.now().replace(month=1, day=1)
current_year_last_date = current_year_first_date.replace(year=current_year_first_date.year + 1) - timedelta(days=1)

daily_time_sheet_date = current_year_first_date
daily_time_sheet_id = 1
while daily_time_sheet_date <= current_year_last_date:
    for employee in User.objects.filter(username__in=[user.username for user in user_seeds]):
        if not employee.is_superuser:
            daily_time_sheet = DailyTimeSheet(
                pk=daily_time_sheet_id,
                employee=employee,
                date=daily_time_sheet_date.date()
            )
            seed_items.append(daily_time_sheet)
            daily_time_sheet_id += 1
    daily_time_sheet_date += timedelta(days=1)
