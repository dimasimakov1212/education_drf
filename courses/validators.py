from rest_framework.serializers import ValidationError


GOOD_URL = ['youtube']


def validator_bad_url(value):
    """ Проверка на наличие в материалах недопустимых ссылок кроме youtube.com """

    if 'www.' in value:

        url_split = value.lower().split(".")

        if set(GOOD_URL) & set(url_split):
            pass
        else:
            raise ValidationError('Нельзя использовать ссылки на сторонние ресурсы (допустимо только youtube.com)')
