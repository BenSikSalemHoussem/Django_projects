
from django.http import HttpResponse
from django.shortcuts import render

from contactApp.forms import contactform2, contactform3
from contactApp.models import Contact

def contact_form(request):
    if request.method == 'POST':
        f = request.POST['firstname']
        l = request.POST['lastname']
        e = request.POST['email']
        m = request.POST['message']
        c = Contact.objects.create(firstname=f, lastname=l, email=e, message=m)
        return HttpResponse('<h2> Data has been submitted</h2>')
    
    return render(request, "myform1.html")

def contact_form2(request):
    if request.method == 'POST':
        form = contactform2(request.POST)
        if form.is_valid():
            fn = form.cleaned_data['firstname']
            ln = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            msg = form.cleaned_data['message']
            c = Contact.objects.create(firstname = fn,
                                       lastname = ln,
                                       email = email,
                                       message = msg)
            return HttpResponse('<h2> Data has been submitted</h2>')
    else :
        form = contactform2()

    return render(request, 'myform2.html', {'mycontact2':form})


def contact_form3(request):
    if request.method == 'POST':
        form = contactform3(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2> Data has been submitted</h2>')
    else :
        form = contactform3()
    return render(request, 'myform3.html', {'mycontact3':form})

