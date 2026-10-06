from django.urls import path
from first_sub_app.profile_view import profil_view
from first_sub_app.views import hello_view

urlpatterns = [
    path('home/', hello_view, name='test'),
    path('profil/', profil_view, name='profil'),
]
