from rest_framework import serializers

from courses.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Course
    """
    # определяем дополнительное поле в модели Course
    lessons_count = serializers.SerializerMethodField()  # данные о количестве уроков в курсе

    class Meta:
        model = Course
        # fields = ('course_title', 'course_description',)
        fields = '__all__'

    def get_lessons_count(self, instance):
        """
        Метод определения поля lessons_count
        :return: количество уроков курса
        """
        return instance.lesson.all().count()


class LessonSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Course
    """
    class Meta:
        model = Lesson
        # fields = ('lesson_title', 'lesson_description',)
        fields = '__all__'
