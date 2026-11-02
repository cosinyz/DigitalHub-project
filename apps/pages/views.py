from django.shortcuts import render

from .models import Service


def home(request):
    services = Service.objects.all()[:3]
    return render(request, 'index.html', {'services': services})


def service_list(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})
