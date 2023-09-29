from django.shortcuts import render
from rest_framework import viewsets, generics

from courses.models import Course, Lesson
from courses.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet-класс для вывода списка курсов и информации по одному объекту
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    """
    класс для создания урока на основе generics
    """
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """
    класс для вывода списка уроков на основе generics
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    класс для вывода одного урока на основе generics
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    класс для изменения урока на основе generics
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    класс для удаления одного мото на основе generics
    """
    queryset = Lesson.objects.all()
