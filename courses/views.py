from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from courses.models import Course, Lesson, Subscription
from courses.paginators import CourseLessonPaginator
from courses.permissions import IsMember, IsModerator, IsOwner, CoursePermission
from courses.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from users.models import UserRoles


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet-класс для вывода списка курсов и информации по одному объекту
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # доступно только авторизованным пользователям и с определенными правами
    permission_classes = [IsAuthenticated, CoursePermission]

    pagination_class = CourseLessonPaginator  # пагинация

    def get_queryset(self):
        """
        Определяем параметры вывода объектов
        :return:
        """
        if self.request.user.user_role == UserRoles.MODERATOR:
            return Course.objects.all()

        else:
            return Course.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
        Определяем порядок создания нового объекта
        """
        new_course = serializer.save()
        new_course.owner = self.request.user  # задаем владельца курса
        new_course.save()


class LessonCreateAPIView(generics.CreateAPIView):
    """
    класс для создания урока на основе generics
    """
    serializer_class = LessonSerializer

    # доступно только авторизованным пользователям и не модераторам
    permission_classes = [IsAuthenticated, IsMember]

    def perform_create(self, serializer):
        """
        Определяем порядок создания нового объекта
        """
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user  # задаем владельца урока
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """
    класс для вывода списка уроков на основе generics
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    # доступно только авторизованным пользователям, модераторам или владельцам
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    pagination_class = CourseLessonPaginator  # пагинация


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    класс для вывода одного урока на основе generics
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    # доступно только авторизованным пользователям, модераторам или владельцам
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    класс для изменения урока на основе generics
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    # доступно только авторизованным пользователям, модераторам или владельцам
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    класс для удаления одного мото на основе generics
    """
    queryset = Lesson.objects.all()

    # доступно только авторизованным владельцам
    permission_classes = [IsAuthenticated, IsOwner]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """
    класс для создания подписки
    """
    serializer_class = SubscriptionSerializer

    # доступно только авторизованным пользователям
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Определяем порядок создания нового объекта
        """
        new_subscription = serializer.save()
        new_subscription.user = self.request.user  # задаем подписчика
        new_subscription.save()


class SubscriptionUpdateAPIView(generics.UpdateAPIView):
    """
    класс для изменения подписки
    """
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    # доступно только авторизованным пользователям, модераторам или владельцам
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
