from django.db import models
from django.contrib.auth.models import User

from shop.models import Category, Product
from accounts.models import UserInfo, Address


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)
    shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    product_quantity = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)

    def __str__(self):
        return f"{self.cart} {self.user}"

    @property
    def total_order_price(self):
        total_price = self.product.price * self.product_quantity
        return total_price



