from django.shortcuts import render
from rest_framework import viewsets, generics

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    класс для создания пользователя на основе generics
    """
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """
    класс для вывода списка пользователей на основе generics
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    класс для вывода одного пользователя на основе generics
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    класс для изменения пользователя на основе generics
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    класс для удаления пользователя на основе generics
    """
    queryset = User.objects.all()
