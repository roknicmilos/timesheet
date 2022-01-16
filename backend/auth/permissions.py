from rest_framework.permissions import BasePermission


class HasAccessToUserResources(BasePermission):
    USER_PK_KEYS = ['user_pk', 'pk', ]

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_admin or request.user.pk == self._get_user_pk(view=view)

    def _get_user_pk(self, view) -> int:
        for key in self.USER_PK_KEYS:
            if key in view.kwargs:
                return int(view.kwargs.get(key))
        else:
            raise KeyError('Unable to find user ID in view kwargs')


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin
