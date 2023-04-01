from .models import Product
from django import forms


class NewProductForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Product
        fields = ('title','category', 'price_type','price1','price2', 'body', 'address',  'phone_number')

    def save(self, request, commit=True):
        product = self.instance
        product.author = request.user
        super().save()
        return product


class ProductForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Product
        fields = ('title', 'body', 'price_type','price1','price2', 'address', 'category', 'phone_number')


