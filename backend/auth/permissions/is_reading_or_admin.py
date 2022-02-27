from typing import List
from rest_framework.viewsets import ViewSet as BaseViewSet
from main.viewsets import ViewSet as CustomViewSet
from auth.permissions import IsAdmin


class IsReadingOrAdmin(IsAdmin):

    def has_permission(self, request, view):
        readonly_actions = self._get_view_readonly_actions(view)
        if view.action in readonly_actions:
            return True
        return super(IsReadingOrAdmin, self).has_permission(request, view)

    @staticmethod
    def _get_view_readonly_actions(view) -> List[str]:
        if isinstance(view, CustomViewSet):
            return view.get_readonly_actions()
        if isinstance(view, BaseViewSet):
            return ['list', 'retrieve']
        return []
