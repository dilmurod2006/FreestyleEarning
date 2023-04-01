# create users models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
#from Works.models import Workscategory
from django.urls import reverse

# Create Custom class for users models
"""
1-models: 'Country'
2-models: 'City'
3-models: 'Age'
4-models: 'Works category'
5-models: 'ZipCode'
6-models: 'email address'
7-models: 'phone number'
9-models: 'avatars'
10-models: 'CV or o'zi haqida malumot'
"""



class CustomUser(AbstractUser):
    country = CountryField()
    city = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=False)
    #workscategory = models.ForeignKey(Workscategory, on_delete=models.CASCADE)
    zipcode = models.IntegerField(null=True, blank=False)
    phone_number = PhoneNumberField()
    avatar = models.ImageField(upload_to='avatars/', blank=True, default='avatars/default.png')
    description = models.TextField( blank=True)
    # avto date time field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    confirm = models.CharField(null=True, blank=True, max_length=5)

    def __str__(self):
        return self.username


class Saved(models.Model):
    product = models.ForeignKey("Works.Product", on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Comment of " + str(self.author.username)    

