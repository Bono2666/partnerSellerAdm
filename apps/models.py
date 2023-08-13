from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Hero(models.Model):
    image = models.ImageField(upload_to='hero/')
    title = models.CharField(max_length=50)


class Members(models.Model):
    name = models.CharField(max_length=50)
    phone = PhoneNumberField(unique=True)
    ig = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    target = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='avatar/', default='avatar/ic_white_profile.png')
