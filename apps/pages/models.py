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
