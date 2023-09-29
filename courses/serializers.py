from rest_framework import serializers

from courses.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Course
    """
    class Meta:
        model = Course
        # fields = ('course_title', 'course_description',)
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Course
    """
    class Meta:
        model = Lesson
        fields = ('lesson_title', 'lesson_description',)
