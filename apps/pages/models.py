from django.db import models
from django.core.validators import MinValueValidator


class Service(models.Model):
    title = models.CharField('Название услуги', max_length=255)
    description = models.TextField('Описание')
    price = models.DecimalField(
        'Цена',
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    image = models.ImageField('Изображение', upload_to='services/')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField('Имя', max_length=255)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=30, blank=True)
    message = models.TextField('Сообщение')
    created_at = models.DateTimeField('Дата отправки', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.name} — {self.created_at:%Y-%m-%d %H:%M}'
