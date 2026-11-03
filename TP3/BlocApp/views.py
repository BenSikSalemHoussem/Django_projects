from django.shortcuts import render
from django.views.generic import ListView

from BlocApp.models import BlogPost

class BlogView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = "Posts/blogView.html"
    