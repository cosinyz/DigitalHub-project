from django.contrib import admin
from .models import CompanyInfo


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded_year', 'projects_count', 'clients_count', 'specialists_count')
    search_fields = ('name', 'email', 'address')
