from rest_framework import generics


from users.models import User
from users.permissions import IsOwner, IsSuperuser
from users.serializers import UserSerializer, AnyUserSerializer
from rest_framework.permissions import IsAuthenticated


class UserCreateAPIView(generics.CreateAPIView):
    """
    класс для создания пользователя на основе generics
    """
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """
    класс для вывода списка пользователей на основе generics
    """
    serializer_class = AnyUserSerializer
    queryset = User.objects.all()

    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    класс для вывода одного пользователя на основе generics
    """
    # serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):

        if self.request.user == self.get_object():
            return UserSerializer
        else:
            return AnyUserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    класс для изменения пользователя на основе generics
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [IsAuthenticated, IsOwner]


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    класс для удаления пользователя на основе generics
    """
    queryset = User.objects.all()

    permission_classes = [IsAuthenticated, IsOwner | IsSuperuser]
