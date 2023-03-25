from django import forms
from webapp.models import Product, Review
from django.core.validators import MinLengthValidator


class ProductForm(forms.ModelForm):
    title = forms.CharField(validators=(MinLengthValidator(limit_value=2),), required='Навзание')
    description = forms.CharField(validators=(MinLengthValidator(limit_value=5),), widget=forms.Textarea, label='Описание')

    class Meta:
        model = Product
        fields = ('title', 'description', 'category', 'image')
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'category': 'Категория',
            'image': 'Картинка'
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'grade')
        labels = {
            'text': 'Текст',
            'grade': 'Оценка'
        }
