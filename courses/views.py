from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from courses.models import Course, Lesson
from courses.permissions import IsMember, IsModerator, IsOwner
from courses.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet-класс для вывода списка курсов и информации по одному объекту
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    permission_classes = [IsAuthenticated]  # доступно только авторизованным пользователям

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
