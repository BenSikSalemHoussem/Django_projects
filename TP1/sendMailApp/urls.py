from django.urls import path

from .views import send_mail_test


urlpatterns = [
    path('mail/', send_mail_test, name='sendmail')
]