from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:

        # создаем тестового пользователя
        self.user = User.objects.create(user_email='admin@sky.pro')
        self.user.set_password('dima123')
        self.user.save()

        # создаем тестовый курс
        self.course = Course.objects.create(
            course_title='Test',
            course_description='Test',
            owner=self.user
        )

        # аутентификацируем пользователя
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        """ тестирование создания уроков """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"user_email": "admin@sky.pro", "password": "dima123"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # задаем данные для создания урока
        data_lesson = {
            'lesson_title': 'Test',
            'lesson_description': 'Test',
            'lesson_video_url': 'www.youtube.com',
            'course': self.course.pk,
            'owner': self.user.pk
        }

        # создаем урок
        response = self.client.post(
            '/lesson/create/',
            data=data_lesson
        )

        # проверяем ответ на создание урока
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # проверяем ответ на соответствие сохраненных данных
        self.assertEquals(
            response.json(),
            {'id': 2, 'lesson_video_url': 'www.youtube.com', 'lesson_description': 'Test',
             'lesson_title': 'Test', 'lesson_avatar': None, 'course': 2, 'owner': 2}
        )

        # проверяем на существование объектов уроков
        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_list_lesson(self):
        """ тестирование списка уроков """

        # создаем объект урока
        Lesson.objects.create(
            lesson_title='Test',
            lesson_description='Test',
            lesson_video_url='www.youtube.com'
        )

        # получаем список уроков
        response = self.client.get(
            '/lesson/'
        )

        # проверяем ответ на получение списка уроков
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        # проверяем ответ на соответствие сохраненных данных
        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 5, 'lesson_video_url': 'www.youtube.com', 'lesson_description': 'Test',
                 'lesson_title': 'Test', 'lesson_avatar': None, 'course': None, 'owner': None}]}
        )

    def test_detail_lesson(self):
        """ тестирование деталей урока """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"user_email": "admin@sky.pro", "password": "dima123"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # получаем данные пользователя
        user = User.objects.get(pk=self.user.pk)

        # создаем объект урока
        lesson = Lesson.objects.create(
            lesson_title='Test',
            lesson_description='Test',
            lesson_video_url='www.youtube.com',
            owner=user
        )

        # получаем детали урока
        response = self.client.get(
            reverse('courses:lesson_detail', kwargs={'pk': lesson.pk})
        )

        # проверяем ответ на получение урока
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        # проверяем ответ на соответствие сохраненных данных
        self.assertEquals(
            response.json(),
            {'id': 4, 'lesson_video_url': 'www.youtube.com', 'lesson_description': 'Test',
             'lesson_title': 'Test', 'lesson_avatar': None, 'course': None, 'owner': 4}
        )

    def test_change_lesson(self):
        """ тестирование изменения урока """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"user_email": "admin@sky.pro", "password": "dima123"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # получаем данные пользователя
        user = User.objects.get(pk=self.user.pk)

        # создаем объект урока
        lesson = Lesson.objects.create(
            lesson_title='Test',
            lesson_description='Test',
            lesson_video_url='www.youtube.com',
            owner=user
        )

        # данные для изменения урока
        data_lesson_change = {
            'lesson_title': 'Test_1',
        }

        # отправляем запрос для изменения урока
        response = self.client.patch(
            reverse('courses:lesson_change', kwargs={'pk': lesson.pk}),
            data=data_lesson_change
        )

        # проверяем ответ на изменения урока
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        # проверяем ответ на соответствие сохраненных данных
        self.assertEquals(
            response.json(),
            {'id': 1, 'lesson_video_url': 'www.youtube.com', 'lesson_description': 'Test',
             'lesson_title': 'Test_1', 'lesson_avatar': None, 'course': None, 'owner': 1}
        )

    def test_delete_lesson(self):
        """ тестирование удаления урока """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"user_email": "admin@sky.pro", "password": "dima123"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # получаем данные пользователя
        user = User.objects.get(pk=self.user.pk)

        # создаем объект урока
        lesson = Lesson.objects.create(
            lesson_title='Test',
            lesson_description='Test',
            lesson_video_url='www.youtube.com',
            owner=user
        )

        # отправляем запрос для удаления урока
        response = self.client.delete(
            reverse('courses:lesson_delete', kwargs={'pk': lesson.pk}),
        )

        # проверяем ответ на удаление урока
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        # создаем тестового пользователя
        self.user = User.objects.create(user_email='admin@sky.pro')
        self.user.set_password('dima123')
        self.user.save()

        # создаем тестовый курс
        self.course = Course.objects.create(
            course_title='Test',
            course_description='Test',
            owner=self.user
        )

        # аутентификацируем пользователя
        self.client.force_authenticate(user=self.user)

    def test_create_subscription(self):
        """ тестирование создания подписки """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"user_email": "admin@sky.pro", "password": "dima123"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # задаем данные для создания подписки
        data = {
            'course': self.course.pk,
            'owner': self.user.pk,
            'is_active': True
        }

        # создаем подписку
        response = self.client.post(
            '/subscription/create/',
            data=data
        )

        # проверяем ответ на создание подписки
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # проверяем ответ на соответствие сохраненных данных
        self.assertEquals(
            response.json(),
            {'course': 7, 'is_active': True}
        )

        # проверяем на существование объектов уроков
        self.assertTrue(
            Subscription.objects.all().exists()
        )

    def test_change_subscription(self):
        """ тестирование изменения подписки """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"user_email": "admin@sky.pro", "password": "dima123"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # получаем данные пользователя
        user = User.objects.get(pk=self.user.pk)

        course = Course.objects.get(pk=self.course.pk)

        # создаем объект подписки
        subscription = Subscription.objects.create(
            course=course,
            user=user,
            is_active=True
        )

        # данные для изменения подписки
        data_subscription_change = {
            'is_active': 'False',
        }

        # отправляем запрос для изменения подписки
        response = self.client.patch(
            reverse('courses:subscription_change', kwargs={'pk': subscription.pk}),
            data=data_subscription_change
        )

        # проверяем ответ на изменения урока
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        # проверяем ответ на соответствие сохраненных данных
        self.assertEquals(
            response.json(),
            {'course': 6, 'is_active': False}
        )
