from django.db import models
from django.utils import timezone


class CompanyInfo(models.Model):
    name = models.CharField('Название компании', max_length=255)
    description = models.TextField('Описание')
    founded_year = models.PositiveSmallIntegerField('Год основания', default=0)
    projects_count = models.PositiveIntegerField('Количество проектов', default=0)
    clients_count = models.PositiveIntegerField('Количество клиентов', default=0)
    specialists_count = models.PositiveIntegerField('Количество специалистов', default=0)
    logo = models.ImageField(
        'Логотип',
        upload_to='company/logos/',
        blank=True,
    )
    phone = models.CharField('Номер телефона', max_length=30)
    email = models.EmailField('Email')
    address = models.CharField('Адрес', max_length=255)
    instagram_url = models.URLField('Instagram', blank=True)
    telegram_url = models.URLField('Telegram', blank=True)
    whatsapp_url = models.URLField('WhatsApp', blank=True)
    youtube_url = models.URLField('YouTube', blank=True)

    class Meta:
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компании'

    @property
    def years_in_business(self):
        if not self.founded_year:
            return 0
        return max(0, timezone.localdate().year - self.founded_year)

    def __str__(self):
        return self.name
