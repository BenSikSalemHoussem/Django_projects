from django.urls import path

from .views import contact_form, contact_form2, contact_form3


urlpatterns = [
    path('myform1/', contact_form, name='newContact'),
    path('myform2/', contact_form2, name='newContact2'),
    path('myform3/', contact_form3, name='newContact3')
]