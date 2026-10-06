
from django.urls import path

from .views import about_view, home_view


urlpatterns = [
    path('home/', home_view, name='homeUrl'),
    path('about/', about_view, name='aboutUrl'),
]
