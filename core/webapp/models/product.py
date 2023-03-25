from django.db import models
from django.db.models import TextChoices
from django.db.models import Avg
from .review import Review


class CategoryChoice(TextChoices):
    SMARTPHONE = 'Smartphone', 'Смартфоны'
    PC = 'Pc', 'Пк'


class Product(models.Model):
    title = models.CharField(
        verbose_name='Название',
        null=False,
        blank=False,
        max_length=70
    )
    category = models.CharField(
        verbose_name='Категория',
        choices=CategoryChoice.choices,
        null=False,
        blank=False,
        max_length=70
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
        max_length=2800,
        default='Описание'
    )
    image = models.ImageField(
        verbose_name='Картина',
        null=True,
        blank=True,
        upload_to='img'
    )

    def __str__(self):
        return f'{self.title} - {self.category}'

    def get_avg(self):
        return self.review_product.aggregate(Avg('grade'))
