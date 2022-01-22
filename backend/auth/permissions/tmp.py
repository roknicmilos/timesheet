from django.urls import resolve
from rest_framework.permissions import BasePermission


class Tmp(BasePermission):
    USER_PK_KEYS = ['user_pk', 'pk', ]

    def has_permission(self, request, view):
        action_name = self._get_action_name(request=request)

        return True

    @staticmethod
    def _get_action_name(request) -> str | None:
        resolve_match = resolve(request.path)

        if resolve_match.url_name.endswith('-detail'):
            if request.method == 'GET':
                return 'retrieve'
            if request.method == 'DELETE':
                return 'destroy'
            if request.method == 'PUT':
                return 'update'
            if request.method == 'PATCH':
                return 'partial_update'

        if resolve_match.url_name.endswith('-list'):
            if request.method == 'GET':
                return 'list'
            if request.method == 'POST':
                return 'create'
            if request.method == 'OPTIONS':
                return 'options'
