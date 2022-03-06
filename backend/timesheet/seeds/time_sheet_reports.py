import random
from timesheet.models import TimeSheetReport
from auth.models import User
from auth.seeds.users import seed_items as user_seeds
from projects.models import Project, Category
from projects.seeds.project_seeds import seed_items as project_seeds
from projects.seeds.categories import seed_items as category_seeds


seed_items = []

projects = list(Project.objects.filter(pk__in=[project.pk for project in project_seeds]))
if not projects:
    raise ValueError('Unable to seed Time Sheet Reports because there are no Projects')

categories = list(Category.objects.filter(pk__in=[category.pk for category in category_seeds]))
if not categories:
    raise ValueError('Unable to seed Time Sheet Reports because there are no Categories')

time_sheet_report_id = 1
for employee in User.objects.filter(pk__in=[user.pk for user in user_seeds]):
    if employee.is_superuser:
        continue

    for index, daily_time_sheet in enumerate(employee.daily_time_sheets.all()[:100]):
        if index % 5:
            # Create a single Time Sheet Report for the given employee and daily time sheet:
            time_sheet_report = TimeSheetReport(
                pk=time_sheet_report_id,
                hours=8,
                overtime_hours=0,
                daily_time_sheet=daily_time_sheet,
                project=random.choice(projects),
                category=random.choice(categories),
            )
            time_sheet_report_id += 1
            seed_items.append(time_sheet_report)
            continue

        # Create two Time Sheet Reports for the given employee and daily time sheet:
        first_time_sheet_report = TimeSheetReport(
            pk=time_sheet_report_id,
            hours=6,
            overtime_hours=0,
            daily_time_sheet=daily_time_sheet,
            project=random.choice(projects),
            category=random.choice(categories),
        )
        time_sheet_report_id += 1

        second_time_sheet_report = TimeSheetReport(
            pk=time_sheet_report_id,
            hours=3,
            overtime_hours=1,
            daily_time_sheet=daily_time_sheet,
            project=random.choice(projects),
            category=random.choice(categories),
        )
        time_sheet_report_id += 1

        seed_items.extend([
            first_time_sheet_report,
            second_time_sheet_report,
        ])
