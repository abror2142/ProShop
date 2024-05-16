from shop.models import Product
from accounts.models import UserInfo
from cart.models import Cart, Order
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User


class ProductManager:
    def __init__(self, request: HttpRequest, product_id=None, action=None):
        self.request = request

    def get_cart(self):

        customer, created = UserInfo.objects.get_or_create(
            user=self.request.user
        )

        cart, created = Cart.objects.get_or_create(
            user=self.request.user,
            active=True
        )

        orders_in_cart = Order.objects.filter(
            user=self.request.user,
            cart=cart
        )
        return {
            'customer': customer,
            'cart': cart,
            'orders_in_cart': orders_in_cart
        }

    def cart_action(self, product_id, action):
        cart = self.get_cart()['cart']
        product = Product.objects.get(pk=product_id)

        cart_product, created = Order.objects.get_or_create(
            cart=cart,
            user=self.request.user,
            product=product
        )

        if action == 'add' and cart_product.product_quantity < product.quantity:
            cart_product.product_quantity += 1
        elif action == 'remove' and cart_product.product_quantity > 0:
            cart_product.product_quantity -= 1

        cart_product.save()

        return {'cart': cart}

