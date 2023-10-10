from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from courses.models import Course, Lesson, Subscription
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


class SubscriptionSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Subscription
    """

    class Meta:
        model = Subscription
        fields = ('course', 'is_active',)


class CourseSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Course
    """

    # задаем валидаторы для описания курса
    course_description = serializers.CharField(validators=[validator_bad_url])

    # определяем дополнительные поля в модели Course
    lessons_count = serializers.SerializerMethodField()  # данные о количестве уроков в курсе
    lessons = serializers.SerializerMethodField()  # данные о уроках курса
    subscription = serializers.SerializerMethodField()  # данные о подписке на курс

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

    def get_subscription(self, course):
        """
        Метод определения поля subscription
        :return: статус подписки на курс
        """

        request = self.context.get("request")  # получение данных

        user = request.user  # получаем текущего пользователя

        subscriptions = Subscription.objects.filter(course=course)  # получаем все подписки курса

        for subscription in subscriptions:

            # проверяем является ли текущий пользователь подписан на курс
            if subscription.user == user:
                user_subscription = subscription.is_active

                return user_subscription
