from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from courses.models import Course, Lesson
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

        # проверяем ответ на создание пользователя
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # проверяем ответ на соответствие сохраненных данных
        self.assertEquals(
            response.json(),
            {'id': 1, 'lesson_video_url': 'www.youtube.com', 'lesson_description': 'Test',
             'lesson_title': 'Test', 'lesson_avatar': None, 'course': 1, 'owner': 1}
        )

        # проверяем на существование объектов уроков
        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_list_lesson(self):
        """ тестирование списка уроков """

        Lesson.objects.create(
            lesson_title='Test',
            lesson_description='Test',
            lesson_video_url='www.youtube.com'
        )

        response = self.client.get(
            '/lesson/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 1, 'lesson_video_url': 'www.youtube.com', 'lesson_description': 'Test',
                 'lesson_title': 'Test', 'lesson_avatar': None, 'course': None, 'owner': None}]}
        )

    def test_detail_lesson(self):
        """ тестирование деталей урока """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"user_email": "admin@sky.pro", "password": "dima123"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        user = User.objects.get(pk=self.user.pk)

        lesson = Lesson.objects.create(
            lesson_title='Test',
            lesson_description='Test',
            lesson_video_url='www.youtube.com',
            owner=user
        )

        response = self.client.get(
            reverse('courses:lesson_detail', kwargs={'pk': lesson.pk})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'lesson_video_url': 'www.youtube.com', 'lesson_description': 'Test',
             'lesson_title': 'Test', 'lesson_avatar': None, 'course': None, 'owner': 1}
        )

    def test_change_lesson(self):
        """ тестирование изменения урока """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"user_email": "admin@sky.pro", "password": "dima123"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        user = User.objects.get(pk=self.user.pk)

        lesson = Lesson.objects.create(
            lesson_title='Test',
            lesson_description='Test',
            lesson_video_url='www.youtube.com',
            owner=user
        )

        data_lesson_change = {
            'lesson_title': 'Test_1',
        }

        response = self.client.patch(
            reverse('courses:lesson_change', kwargs={'pk': lesson.pk}),
            data=data_lesson_change
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'lesson_video_url': 'www.youtube.com', 'lesson_description': 'Test',
             'lesson_title': 'Test_1', 'lesson_avatar': None, 'course': None, 'owner': 1}
        )



