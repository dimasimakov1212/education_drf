from django.conf import settings
from django.db import models


class Course(models.Model):
    """
    Класс для создания курса
    """
    course_title = models.CharField(max_length=150, verbose_name='название')
    course_description = models.TextField(verbose_name='описание')
    course_avatar = models.ImageField(upload_to='media/', verbose_name='аватар', blank=True, null=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец',
                              blank=True, null=True)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.course_title}'

    class Meta:
        verbose_name = 'Курс'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Курсы'  # Настройка для наименования набора объектов
        ordering = ('course_title',)  # сортировка по наименованию


class Lesson(models.Model):
    """
    Класс для создания урока
    """
    lesson_title = models.CharField(max_length=150, verbose_name='название')
    lesson_description = models.TextField(verbose_name='описание')
    lesson_avatar = models.ImageField(upload_to='media/', verbose_name='аватар', blank=True, null=True)
    lesson_video_url = models.URLField(verbose_name='Ссылка на видео', blank=True, null=True)
    lesson_datetime_changing = models.DateTimeField(blank=True, null=True,
                                                    verbose_name='Дата и время последнего изменения')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', blank=True, null=True,
                               related_name='lesson')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец',
                              blank=True, null=True)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.lesson_title}'

    class Meta:
        verbose_name = 'Урок'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Уроки'  # Настройка для наименования набора объектов
        ordering = ('lesson_title',)  # сортировка по наименованию


class Subscription(models.Model):
    """
    Модель подписки на курсы
    """

    VERSION_CHOICES = ((True, 'Подписан'), (False, 'Не подписан'))

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь',
                             blank=True, null=True)
    is_active = models.BooleanField(choices=VERSION_CHOICES, default=True, verbose_name='Статус подписки')
