from datetime import timedelta, date
from typing import List
from django.utils import timezone
from freezegun import freeze_time
from rest_framework.reverse import reverse
from auth.factories import UserFactory
from main.utils import format_datetime
from projects.factories import ProjectFactory, CategoryFactory
from timesheet.factories import DailyTimeSheetFactory
from timesheet.models import DailyTimeSheet
from main.tests.mixins import APITestCase


class TestDailyTimeSheetViewSet(APITestCase):

    @classmethod
    def setUpTestData(cls):
        super(TestDailyTimeSheetViewSet, cls).setUpTestData()
        today = timezone.now().date()
        cls.seven_days_ago = today - timedelta(days=7)
        cls.eight_days_ago = today - timedelta(days=8)
        cls.seven_days_ahead = today + timedelta(days=7)
        cls.eight_days_ahead = today + timedelta(days=8)

    def tearDown(self) -> None:
        super(TestDailyTimeSheetViewSet, self).tearDown()
        DailyTimeSheet.objects.all().delete()
        DailyTimeSheetFactory.reset()

    @staticmethod
    def build_daily_time_sheets_list_url(user_id: int, **url_params) -> str:
        base_url = reverse('api:daily-time-sheets-list', args=(user_id,))
        return f'{base_url}?{"&".join([f"{key}={value}" for key, value in url_params.items()])}'

    @staticmethod
    def build_daily_time_sheets_detail_url(pk: int, user_id: int) -> str:
        return reverse('api:daily-time-sheets-detail', args=(user_id, pk))

    def test_should_return_list_of_all_daily_time_sheets_of_the_user(self):
        user = UserFactory.create()
        daily_time_sheets = DailyTimeSheetFactory.create_batch(count=3, employee=user, time_sheet_report_count=3)
        response = self.client.get(reverse('api:daily-time-sheets-list', args=(user.pk,)))
        self.assertEqual(response.status_code, 200)
        actual_response_data = response.json()
        self.assertIsInstance(actual_response_data, list)
        self.assertEqual(len(actual_response_data), len(DailyTimeSheet.objects.all()))
        expected_response_data = self._get_expected_list_response_data(daily_time_sheets=daily_time_sheets)
        self.assertEqual(actual_response_data, expected_response_data)

    @classmethod
    def _get_expected_list_response_data(cls, daily_time_sheets: List[DailyTimeSheet]) -> List[dict]:
        expected_data = []
        for daily_time_sheet in daily_time_sheets:
            expected_data_item = cls._get_expected_detail_response_data(daily_time_sheet=daily_time_sheet)
            expected_data.append(expected_data_item)
        return expected_data

    @staticmethod
    def _get_expected_detail_response_data(daily_time_sheet: DailyTimeSheet) -> dict:
        time_sheet_reports_data = []
        for time_sheet_report in daily_time_sheet.time_sheet_reports.all():
            time_sheet_reports_data.append({
                'id': time_sheet_report.pk,
                'hours': time_sheet_report.hours,
                'overtime_hours': time_sheet_report.overtime_hours,
                'description': time_sheet_report.description,
                'daily_time_sheet': daily_time_sheet.pk,
                'project': time_sheet_report.project.pk,
                'category': time_sheet_report.category.pk,
                'created': format_datetime(datetime=time_sheet_report.created),
                'modified': format_datetime(datetime=time_sheet_report.modified),
            })

        return {
            'id': daily_time_sheet.pk,
            'time_sheet_reports': time_sheet_reports_data,
            'date': daily_time_sheet.date.isoformat(),
            'employee': daily_time_sheet.employee.pk,
            'created': format_datetime(datetime=daily_time_sheet.created),
            'modified': format_datetime(datetime=daily_time_sheet.modified),
        }

    def test_should_return_404_instead_of_daily_time_sheet_list_of_the_user_when_user_does_not_exist(self):
        user = UserFactory.create()
        DailyTimeSheetFactory.create_batch(count=2, employee=user)
        response = self.client.get(reverse('api:daily-time-sheets-list', args=(UserFactory.next_id,)))
        self.assertEqual(response.status_code, 404)
        actual_response_data = response.json()
        expected_response_data = {
            'detail': 'User not found.'
        }
        self.assertEqual(actual_response_data, expected_response_data)

    def test_should_return_daily_time_sheet_list_of_the_user_filtered_by_from_date(self):
        user = UserFactory.create()
        daily_time_sheets = DailyTimeSheetFactory.create_batch(count=3, employee=user)
        self._update_daily_time_sheet_date(daily_time_sheet=daily_time_sheets[0], new_date=self.eight_days_ago)
        url = self.build_daily_time_sheets_list_url(user_id=user.pk, **{'from': self.seven_days_ago.isoformat()})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        actual_response_data = response.json()
        self.assertIsInstance(actual_response_data, list)
        self.assertEqual(len(actual_response_data), len(daily_time_sheets) - 1)
        expected_response_data = self._get_expected_list_response_data(daily_time_sheets=daily_time_sheets[1:])
        self.assertEqual(actual_response_data, expected_response_data)

    @staticmethod
    def _update_daily_time_sheet_date(daily_time_sheet: DailyTimeSheet, new_date: date) -> None:
        daily_time_sheet.date = new_date
        daily_time_sheet.save()

    def test_should_return_daily_time_sheet_list_of_the_user_filtered_by_until_date(self):
        user = UserFactory.create()
        daily_time_sheets = DailyTimeSheetFactory.create_batch(count=3, employee=user)
        self._update_daily_time_sheet_date(daily_time_sheet=daily_time_sheets[-1], new_date=self.eight_days_ahead)
        url = self.build_daily_time_sheets_list_url(user_id=user.pk, until=self.seven_days_ahead.isoformat())
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        actual_response_data = response.json()
        self.assertIsInstance(actual_response_data, list)
        self.assertEqual(len(actual_response_data), len(daily_time_sheets) - 1)
        expected_response_data = self._get_expected_list_response_data(daily_time_sheets=daily_time_sheets[:-1])
        self.assertEqual(actual_response_data, expected_response_data)

    def test_should_return_daily_time_sheet_list_of_the_user_filtered_by_from_and_until_dates(self):
        user = UserFactory.create()
        daily_time_sheets = DailyTimeSheetFactory.create_batch(count=3, employee=user)
        self._update_daily_time_sheet_date(daily_time_sheet=daily_time_sheets[0], new_date=self.eight_days_ago)
        self._update_daily_time_sheet_date(daily_time_sheet=daily_time_sheets[-1], new_date=self.eight_days_ahead)
        url_params = {'from': self.seven_days_ago, 'until': self.seven_days_ahead}
        url = self.build_daily_time_sheets_list_url(user_id=user.pk, **url_params)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        actual_response_data = response.json()
        self.assertIsInstance(actual_response_data, list)
        self.assertEqual(len(actual_response_data), 1)
        expected_response_data = [
            self._get_expected_detail_response_data(daily_time_sheet=daily_time_sheets[1])
        ]
        self.assertEqual(actual_response_data, expected_response_data)

    @freeze_time('2022-01-01')
    def test_should_create_daily_time_sheet_without_time_sheet_reports_and_return_it(self):
        user = UserFactory.create()
        request_data = {
            'time_sheet_reports': [
                {
                    'hours': 8.0,
                    'overtime_hours': 0.0,
                    'description': 'First time sheet report',
                    'daily_time_sheet': 1,
                },
            ],
            'date': DailyTimeSheetFactory.next_date.isoformat(),

        }
        next_id = DailyTimeSheetFactory.next_id
        url = self.build_daily_time_sheets_list_url(user_id=user.pk)
        response = self.client.post(url, json=request_data)
        self.assertEqual(response.status_code, 201)
        actual_response_data = response.json()
        expected_response_data = {
            'id': next_id,
            'employee': user.pk,
            'date': request_data.get('date'),
            'time_sheet_reports': [],
            'created': format_datetime(datetime=timezone.now()),
            'modified': format_datetime(datetime=timezone.now()),
        }
        self.assertEqual(actual_response_data, expected_response_data)

    def test_should_return_404_instead_of_creating_daily_time_sheet_when_user_does_not_exist(self):
        request_data = {
            'date': DailyTimeSheetFactory.next_date.isoformat(),
        }
        url = self.build_daily_time_sheets_list_url(user_id=UserFactory.next_id)
        response = self.client.post(url, json=request_data)
        self.assertEqual(response.status_code, 404)
        actual_response_data = response.json()
        expected_response_data = {
            'detail': 'User not found.'
        }
        self.assertEqual(actual_response_data, expected_response_data)

    def test_should_return_daily_time_sheet_for_the_user(self):
        daily_time_sheet = DailyTimeSheetFactory.create()
        url = self.build_daily_time_sheets_detail_url(
            user_id=daily_time_sheet.employee.pk,
            pk=daily_time_sheet.pk
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        actual_response_data = response.json()
        expected_response_data = self._get_expected_detail_response_data(daily_time_sheet=daily_time_sheet)
        self.assertEqual(actual_response_data, expected_response_data)

    def test_should_return_404_instead_of_daily_time_sheet_when_the_user_does_not_exist(self):
        daily_time_sheet = DailyTimeSheetFactory.create()
        url = self.build_daily_time_sheets_detail_url(user_id=UserFactory.next_id, pk=daily_time_sheet.pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        actual_response_data = response.json()
        expected_response_data = {
            'detail': 'User not found.'
        }
        self.assertEqual(actual_response_data, expected_response_data)

    def test_should_return_404_instead_of_daily_time_sheet_when_it_does_not_exist(self):
        daily_time_sheet = DailyTimeSheetFactory.create()
        url = self.build_daily_time_sheets_detail_url(
            user_id=daily_time_sheet.employee.pk,
            pk=DailyTimeSheetFactory.next_id
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        actual_response_data = response.json()
        expected_response_data = {
            'detail': 'Not found.'
        }
        self.assertEqual(actual_response_data, expected_response_data)

    def test_should_return_404_instead_of_daily_time_sheet_when_daily_time_sheet_does_not_belong_to_the_user(self):
        daily_time_sheet = DailyTimeSheetFactory.create()
        another_daily_time_sheet = DailyTimeSheetFactory.create()
        self.assertNotEqual(daily_time_sheet.employee, another_daily_time_sheet.employee)
        url = self.build_daily_time_sheets_detail_url(
            user_id=daily_time_sheet.employee.pk,
            pk=another_daily_time_sheet.pk
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        actual_response_data = response.json()
        expected_response_data = {
            'detail': 'Not found.'
        }
        self.assertEqual(actual_response_data, expected_response_data)

    @freeze_time('2022-01-01')
    def test_should_only_update_time_sheet_report_by_overriding_all_of_them(self):
        daily_time_sheet = DailyTimeSheetFactory.create(time_sheet_report_count=3)
        self.assertEqual(daily_time_sheet.time_sheet_reports.count(), 3)
        time_sheet_reports = list(daily_time_sheet.time_sheet_reports.all())
        another_user = UserFactory.create()
        self.assertNotEqual(daily_time_sheet.employee, another_user)
        url = self.build_daily_time_sheets_detail_url(
            user_id=daily_time_sheet.employee.pk,
            pk=daily_time_sheet.pk
        )
        new_project = ProjectFactory.create()
        new_category = CategoryFactory.create()
        time_sheet_reports_data = [
            {
                'hours': time_sheet_reports[0].hours + 1,
                'overtime_hours': time_sheet_reports[0].overtime_hours,
                'description': time_sheet_reports[0].description,
                'daily_time_sheet': daily_time_sheet.pk,
                'project': new_project.pk,
                'category': new_project.pk,
            },
            {
                'hours': time_sheet_reports[1].hours,
                'overtime_hours': time_sheet_reports[1].overtime_hours + 1,
                'description': f'{time_sheet_reports[1].description} updated',
                'daily_time_sheet': daily_time_sheet.pk,
                'project': new_project.pk,
                'category': new_project.pk,
            },
        ]
        request_data = {
            'time_sheet_reports': time_sheet_reports_data,
            'employee': another_user.pk,
            'date': (daily_time_sheet.date + timedelta(days=1)).isoformat(),
        }
        expected_response_data = self._get_expected_detail_response_data(daily_time_sheet=daily_time_sheet)
        response = self.client.patch(url, json=request_data)
        self.assertEqual(response.status_code, 200)
        actual_response_data = response.json()
        expected_response_data['time_sheet_reports'] = [
            {
                **time_sheet_reports_data[0],
                'id': time_sheet_reports[0].id + len(time_sheet_reports),
                'created': format_datetime(datetime=timezone.now()),
                'modified': format_datetime(datetime=timezone.now()),
            },
            {
                **time_sheet_reports_data[1],
                'id': time_sheet_reports[1].id + len(time_sheet_reports),
                'created': format_datetime(datetime=timezone.now()),
                'modified': format_datetime(datetime=timezone.now()),
            },
        ]
        self.assertEqual(actual_response_data, expected_response_data)
        self.assertEqual(daily_time_sheet.time_sheet_reports.count(), 2)  # the last one should be deleted

    def test_should_return_404_instead_of_updating_daily_time_sheet_when_user_does_not_exits(self):
        daily_time_sheet = DailyTimeSheetFactory.create()
        url = self.build_daily_time_sheets_detail_url(user_id=UserFactory.next_id, pk=daily_time_sheet.pk)
        response = self.client.patch(url, json={})
        self.assertEqual(response.status_code, 404)
        actual_response_data = response.json()
        expected_response_data = {
            'detail': 'User not found.'
        }
        self.assertEqual(actual_response_data, expected_response_data)

    def test_should_return_404_instead_of_updating_daily_time_sheet_when_it_does_not_exits(self):
        user = UserFactory.create()
        url = self.build_daily_time_sheets_detail_url(user_id=user.pk, pk=DailyTimeSheetFactory.next_id)
        response = self.client.patch(url, json={})
        self.assertEqual(response.status_code, 404)
        actual_response_data = response.json()
        expected_response_data = {
            'detail': 'Not found.'
        }
        self.assertEqual(actual_response_data, expected_response_data)

    def test_should_return_404_instead_of_updating_daily_time_sheet_when_daily_time_sheet_does_not_belong_to_the_user(
            self):
        daily_time_sheet = DailyTimeSheetFactory.create()
        another_daily_time_sheet = DailyTimeSheetFactory.create()
        url = self.build_daily_time_sheets_detail_url(
            user_id=daily_time_sheet.employee.pk,
            pk=another_daily_time_sheet.pk
        )
        response = self.client.patch(url, json={})
        self.assertEqual(response.status_code, 404)
        actual_response_data = response.json()
        expected_response_data = {
            'detail': 'Not found.'
        }
        self.assertEqual(actual_response_data, expected_response_data)
