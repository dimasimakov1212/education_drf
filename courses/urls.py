from django.urls import path

from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionCreateAPIView, SubscriptionUpdateAPIView, \
    SubscriptionListAPIView

app_name = CoursesConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_change'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/subscription_list/', SubscriptionListAPIView.as_view(), name='subscription_list'),
    path('subscription/update/<int:pk>/', SubscriptionUpdateAPIView.as_view(), name='subscription_change'),
    ] + router.urls
