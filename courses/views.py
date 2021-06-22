from django.shortcuts import render
from courses.models import Course


def home_view(request):
    object_list = Course.objects.all()
    return render(request, 'home.html', {
        'object_list': object_list,
        'nav': 'home'
    })


def about_view(request):
    return render(request, 'about.html', {
        'nav': 'about'
    })
