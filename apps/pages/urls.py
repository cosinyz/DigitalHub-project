from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('services/', views.service_list, name='services'),
    path('contacts/', views.contacts, name='contacts'),
]
