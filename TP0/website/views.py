from django.shortcuts import render

def home_view(request) :
    context = {'name': 'Houssem',
               'class': 'GLSI'}
    return render(request, 'website/home.html', context=context)

def about_view(request) :
    return render(request, 'website/about.html')