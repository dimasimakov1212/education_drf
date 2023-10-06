from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsMember(BasePermission):
    """
    Задаем права обычных пользователей
    """
    def has_permission(self, request, view):
        if request.user.user_role == UserRoles.MEMBER:
            return True

        return False


class IsModerator(BasePermission):
    """
    Задаем права модераторов
    """
    def has_permission(self, request, view):
        if request.user.user_role == UserRoles.MODERATOR:
            return True

        return False


class IsOwner(BasePermission):
    """
    Задаем права владельцев объектов
    """
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True

        return False
