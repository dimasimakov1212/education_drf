from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices):
    """
    Определяет роль поли пользователей
    """
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None
    VERSION_CHOICES = ((True, 'Действующий'), (False, 'Заблокирован'))

    user_email = models.EmailField(unique=True, verbose_name='почта')
    user_phone = models.CharField(max_length=35, verbose_name='телефон', blank=True, null=True)
    user_avatar = models.ImageField(upload_to='media/', verbose_name='аватар', blank=True, null=True)
    user_city = models.CharField(max_length=100, verbose_name='город', blank=True, null=True)
    is_active = models.BooleanField(choices=VERSION_CHOICES, default=True, verbose_name='Статус пользователя')

    user_role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = "user_email"
    REQUIRED_FIELDS = []
