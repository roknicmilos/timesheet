from django_filters import BooleanFilter
from django_filters.constants import EMPTY_VALUES


class HasOvertimeBooleanField(BooleanFilter):

    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        self.lookup_expr = 'gt' if value else 'exact'
        return super(HasOvertimeBooleanField, self).filter(qs, 0)
