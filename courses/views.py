from django.shortcuts import render
from rest_framework import viewsets

from courses.models import Course
from courses.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet-класс для вывода списка авто и информации по одному объекту
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
