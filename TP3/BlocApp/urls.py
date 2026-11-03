from django.contrib import admin
from django.urls import path

from BlocApp.views import BlogView

urlpatterns = [
    path('blogapp/', BlogView.as_view(), name="listhtml"),
]