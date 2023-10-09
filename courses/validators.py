from rest_framework.serializers import ValidationError


GOOD_URL = ['youtube']


def validator_bad_url(value):
    """ Проверка на наличие в материалах недопустимых ссылок кроме youtube.com """

    url_split = value.lower().split(".")

    # if GOOD_URL not in url_split:
    #     raise ValidationError('Нельзя использовать ссылки на сторонние ресурсы (допустимо только youtube.com)')

    if set(GOOD_URL) & set(url_split):
        pass
    else:
        raise ValidationError('Нельзя использовать ссылки на сторонние ресурсы (допустимо только youtube.com)')
