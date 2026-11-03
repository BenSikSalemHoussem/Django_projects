from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import render

from sendMailApp.forms import contactForm

def send_mail_test(request):
    if request.method == 'GET':
        form = contactForm()
    else :
        form = contactForm(request.POST)
        if form.is_valid():
            emailList = []
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            mesage = form.cleaned_data['mesage']
            to_email = form.cleaned_data['to_email']
            emailList.append(to_email)
            
            try:
                send_mail(subject, mesage, from_email, emailList)
            except BadHeaderError:
                return HttpResponse('<h2>Invalid Header: mail not send</h2>')

            return HttpResponse('<h2>Submitted :)</h2>')
    return render(request, 'email.html', {'form':form})
