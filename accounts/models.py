from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    choose_products = models.ManyToManyField('products.Product', related_name='choose_users')
    followers = models.ManyToManyField('accounts.User', related_name='followings')
    