from datetime import timedelta
from django.db import IntegrityError
from django.test import TransactionTestCase
from core.factories import UserFactory, DailyTimeSheetFactory
from core.models import DailyTimeSheet


class BaseManagerTests(TransactionTestCase):

    def tearDown(self) -> None:
        super(BaseManagerTests, self).tearDown()
        DailyTimeSheet.objects.all().delete()

    def assertNewDailyTimeSheet(self, obj: DailyTimeSheet, **kwargs) -> None:
        self.assertEqual(obj.date, kwargs.get('date'))
        self.assertEqual(obj.employee, kwargs.get('employee'))

    def test_should_create_multiple_daily_time_sheets(self):
        user = UserFactory.create()
        kwargs_list = [
            {'date': DailyTimeSheetFactory.next_date, 'employee': user, },
            {'date': DailyTimeSheetFactory.next_date + timedelta(days=1), 'employee': user, },
        ]
        daily_time_sheets = DailyTimeSheet.objects.create_batch(*kwargs_list)
        self.assertEqual(len(daily_time_sheets), len(kwargs_list))
        for daily_time_sheet, kwargs in zip(daily_time_sheets, kwargs_list):
            self.assertNewDailyTimeSheet(daily_time_sheet, **kwargs)

    def test_should_not_create_any_daily_time_sheet_if_error_is_raised(self):
        self.assertFalse(DailyTimeSheet.objects.exists())
        single_kwargs = {
            'date': DailyTimeSheetFactory.next_date,
            'employee': UserFactory.create(),
        }

        # Test if kwargs are valid and will create a single object
        daily_time_sheet = DailyTimeSheet.objects.create(**single_kwargs)
        self.assertNewDailyTimeSheet(daily_time_sheet, **single_kwargs)
        daily_time_sheet.delete()
        self.assertFalse(DailyTimeSheet.objects.exists())

        kwargs_list = [single_kwargs, single_kwargs]
        # Second kwargs "date" is not unique, and it should raise error:
        try:
            DailyTimeSheet.objects.create_batch(*kwargs_list)
            self.fail('Did not raise IntegrityError')
        except IntegrityError:
            self.assertFalse(DailyTimeSheet.objects.exists())
