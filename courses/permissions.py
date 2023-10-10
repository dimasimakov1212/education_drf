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


class CoursePermission(BasePermission):
    """
    Задаем права доступа для CourseViewSet
    """

    def has_permission(self, request, view):
        """
        Права доступа к действиям
        """

        # права доступа для просмотра и изменения курсов у модераторов и пользователей
        if view.action in ['list', 'retrieve', 'update', 'partial_update']:
            if request.user.user_role == UserRoles.MODERATOR or request.user.user_role == UserRoles.MEMBER:
                return True

        # права доступа для создания и удаления курсов только у пользователей
        elif view.action in ['create', 'destroy']:
            if request.user.user_role == UserRoles.MEMBER:
                return True

        else:
            return False

    def has_object_permission(self, request, view, obj):
        """
        Права доступа к объектам
        """

        # права доступа для просмотра и изменения курсов у модераторов и владельцев
        if view.action in ['retrieve', 'update', 'partial_update']:
            if request.user == obj.owner or request.user.user_role == UserRoles.MODERATOR:
                return True

        # права доступа для удаления курсов только у владельцев
        elif view.action == 'destroy':
            if request.user == obj.owner:
                return True

        else:
            return False


class IsSubscriber(BasePermission):
    """
    Задаем права подписчиков
    """
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True

        return False
