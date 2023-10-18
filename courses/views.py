from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from datetime import datetime, timedelta
import pytz

from courses.models import Course, Lesson, Subscription
from courses.paginators import CourseLessonPaginator
from courses.permissions import IsMember, IsModerator, IsOwner, CoursePermission, IsSubscriber
from courses.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from users.models import UserRoles
from courses.tasks import subscriber_notice


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet-класс для вывода списка курсов и информации по одному объекту
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # доступно только авторизованным пользователям и с определенными правами
    permission_classes = [IsAuthenticated, CoursePermission]
    # permission_classes = [AllowAny]

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
    # permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """
        Определяем порядок создания нового объекта
        """
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user  # задаем владельца урока
        new_lesson.lesson_datetime_changing = datetime.now()  # заносим текущие дату и время в последние изменения урока
        new_lesson.save()

        # запускаем отложенную задачу по информированию подписчиков курса о добалении нового урока
        subscriber_notice.delay(new_lesson.course_id)


class LessonListAPIView(generics.ListAPIView):
    """
    класс для вывода списка уроков на основе generics
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    # доступно только авторизованным пользователям, модераторам или владельцам
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    # permission_classes = [AllowAny]

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

    def perform_update(self, serializer):
        """
        Определяем порядок изменения урока
        """
        changed_lesson = serializer.save()
        date_time_now = datetime.now()  # получаем текущие дату и время
        moscow_timezone = pytz.timezone('Europe/Moscow')  # устанавливаем часовой пояс
        date_now = date_time_now.astimezone(moscow_timezone)  # устанавливаем текущую дату с учетом часового пояса

        # если дата последнего изменения урока существует, проверяем условие запуска отложенной задачи
        if changed_lesson.lesson_datetime_changing:

            # устанавливаем дату последнего изменения урока с учетом часового пояса
            lesson_last_change_date = changed_lesson.lesson_datetime_changing.astimezone(moscow_timezone)

            # если текущее время больше времени последнего изменения урока на количество часов
            if abs(date_now - lesson_last_change_date) > timedelta(hours=4):
                # запускаем отложенную задачу по информированию подписчиков курса о изменениях уроков курса
                subscriber_notice.delay(changed_lesson.course_id)

        # заносим текущие дату и время в последние изменения урока
        changed_lesson.lesson_datetime_changing = date_now
        changed_lesson.save()


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


class SubscriptionListAPIView(generics.ListAPIView):
    """
    класс для вывода списка подписок
    """
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    # доступно только авторизованным пользователям, модераторам или владельцам
    # permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    permission_classes = [AllowAny]


class SubscriptionUpdateAPIView(generics.UpdateAPIView):
    """
    класс для изменения подписки
    """
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    # доступно только авторизованным пользователям, модераторам или владельцам
    permission_classes = [IsAuthenticated, IsModerator | IsSubscriber]
