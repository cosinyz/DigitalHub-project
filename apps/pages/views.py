from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import ContactMessageForm
from .models import Service


@require_http_methods(['GET', 'POST'])
def contacts(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо! Ваша заявка отправлена.')
            return redirect('pages:contacts')
    else:
        form = ContactMessageForm()

    return render(request, 'contacts.html', {'form': form})


def home(request):
    services = Service.objects.all()[:3]
    return render(request, 'index.html', {'services': services})


def service_list(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})
