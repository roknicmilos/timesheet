import random
from datetime import date, timedelta
from django.utils import timezone


def get_random_date() -> date:
    return timezone.now() - timedelta(days=random.randint(-30, 30))
