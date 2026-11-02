from django.db import models


class CompanyInfo(models.Model):
    name = models.CharField('Название компании', max_length=255)
    description = models.TextField('Описание')
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

    def __str__(self):
        return self.name
