from django.shortcuts import get_object_or_404, redirect, render

from meetings.forms import MeetingForm
from meetings.models import Meeting

def list_meetings(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings/list.html', {'meets':meetings})

def get_view(request, id):
    meeting = get_object_or_404(Meeting,id=id)
    return render(request, 'meetings/details.html', {'meeting':meeting})

def del_meeting(request,id):
    meeting = get_object_or_404(Meeting, id=id)
    if request.method == 'POST' :
        meeting.delete()
        return redirect('listMeetings')
    return render(request, 'meetings/confirm_delete.html', {'meeting': meeting})

def new_meeting(request):
    form = MeetingForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listMeetings')
        form = MeetingForm()

    return render(request, 'meetings/new.html', {'form': form})

def update_meeting(request, id):
    meeting = get_object_or_404(Meeting, id=id)

    if request.method == 'POST' :
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('listMeetings')
    else:
        form = MeetingForm(instance=meeting)
    
    return render(request, 'meetings/update.html', {'form': form})