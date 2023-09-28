from django.urls import path

from courses.apps import CoursesConfig


app_name = CoursesConfig.name

urlpatterns = [
    # path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    ]
