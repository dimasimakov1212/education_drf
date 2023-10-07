from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsOwner(BasePermission):
    """
    Задаем права владельцев объектов
    """
    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True

        return False


class IsSuperuser(BasePermission):
    """
    Задаем права суперюзера
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        return False
