from celery import shared_task

from courses.models import Course, Subscription


@shared_task
def subscriber_notice(course_id):
    """
    Уведомление подписчиков об изменениях курса
    """

    course = Course.objects.filter(pk=course_id)

    subscriptions = Subscription.objects.filter(course=course_id)

    for a in subscriptions:
        print(a.user)

    # if instance:
    #
    #     for subscription in instance.subscription.all():
    #         if subscription:
    #             print(f'Привет {subscription.user}! В курсе {instance.course_title} произошли изменения')
