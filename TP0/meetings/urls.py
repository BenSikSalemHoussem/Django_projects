from django.urls import path

from .views import del_meeting, get_view, list_meetings


urlpatterns = [
    path('list_meetings/', list_meetings, name='listMeetings'),
    path('details/<int:id>/', get_view, name='getMeet'),
    path('delete/<int:id>/', del_meeting, name='delMeet'),
]
