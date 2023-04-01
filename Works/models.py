from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from Accounts.models import CustomUser


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Category, related_name='products', null=True, blank=False, on_delete=models.CASCADE)
    UZ = "so'm"
    US = "$"
    the_price = ((UZ, "so'm"), (US, "$"))
    price_type = models.CharField(max_length=10, choices=the_price, default="so'm")
    price1 = models.IntegerField(null=True, blank=False)
    price2 = models.IntegerField(null=True, blank=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    address = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.category)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Comment of " + str(self.author.username)