from django.shortcuts import render, redirect
from utils.product_manager import ProductManager


def cart_view(request):
    data = ProductManager(request).get_cart()
    orders_in_cart = data['orders_in_cart']
    cart = data['cart']
    customer = data['customer']

    context = {
        'cart': cart,
        'orders_in_cart': orders_in_cart,
        'customer': customer
    }
    print(cart)
    return render(request, 'cart.html', context)


def cart_action_view(request, product_id, action):
    cart = ProductManager(request).cart_action(product_id, action)['cart']
    context = {
        'cart': cart
    }
    print(cart.order_set.all())
    return redirect('cart')
