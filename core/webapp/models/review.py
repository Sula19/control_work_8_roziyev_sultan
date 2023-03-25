from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import IntegerChoices


class GradeChoice(IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class Review(models.Model):
    author = models.ForeignKey(
        to=get_user_model(),
        related_name='author',
        verbose_name='Автор',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to='webapp.Product',
        related_name='review_product',
        verbose_name='Продукт',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name='Текст отзыва',
        null=False,
        blank=False,
        max_length=3000
    )
    grade = models.IntegerField(
        choices=GradeChoice.choices,
        verbose_name='Оценка',
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.author} - {self.text} - {self.grade}'
