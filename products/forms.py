from dataclasses import field
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = (
            "user",
            "cart",
            "review",
            "qna",
        )
        # field = ['name', 'price', 'thumbnail', 'image', 'content']