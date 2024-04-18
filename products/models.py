from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    price = models.PositiveIntegerField()
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
