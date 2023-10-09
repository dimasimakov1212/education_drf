from rest_framework import serializers

from courses.models import Course, Lesson
from courses.validators import validator_bad_url


class LessonSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Lesson
    """

    # задаем валидаторы для описания урока и ссылки на видео
    lesson_video_url = serializers.CharField(validators=[validator_bad_url])
    lesson_description = serializers.CharField(validators=[validator_bad_url])

    class Meta:
        model = Lesson
        # fields = ('lesson_title', 'lesson_description',)
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Course
    """

    # задаем валидаторы для описания курса
    course_description = serializers.CharField(validators=[validator_bad_url])

    # определяем дополнительное поле в модели Course
    lessons_count = serializers.SerializerMethodField()  # данные о количестве уроков в курсе
    lessons = serializers.SerializerMethodField()  # данные о уроках курса

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

    def get_lessons(self, course):
        """
        Метод определения поля lessons
        :return: список уроков курса
        """
        lessons = [lesson.lesson_title for lesson in Lesson.objects.filter(course=course)]
        return lessons
