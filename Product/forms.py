from django import forms
from .models import ProductCategory, Product


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "parent_category": forms.Select(attrs={"class": "form-control"})
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "pricing": forms.NumberInput(attrs={"class": "form-control"}),
            "warranty": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"})
        }
