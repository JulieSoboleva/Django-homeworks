import datetime
import os

from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    template_name = 'app/current_time.html'
    context = {
        'time': datetime.datetime.now().time().isoformat()
    }
    return render(request, template_name, context)


def workdir_view(request):
    template_name = 'app/workdir.html'
    context = {
        'files': os.listdir()
    }
    return render(request, template_name, context)
