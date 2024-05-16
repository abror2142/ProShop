from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name="subcategories")

    def __str__(self):
        return self.name


class Measurement(models.Model):
    full_name = models.CharField(max_length=40)
    symbol = models.CharField(max_length=4, null=True, blank=True)
    is_decimal_measurable = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    produced_at = models.DateTimeField(default=now)
    added_at = models.DateTimeField(auto_now_add=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    measurement = models.ForeignKey(Measurement, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

