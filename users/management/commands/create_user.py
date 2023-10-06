from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            user_email='pionof@mail.ru',
            first_name='Dima',
            last_name='Si',
            is_staff=False,
            is_superuser=False
        )

        user.set_password('dima123dima123')
        user.save()
