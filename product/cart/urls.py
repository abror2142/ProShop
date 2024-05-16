from django.urls import path
from .views import cart_view, cart_action_view


urlpatterns = [
    path('', cart_view, name='cart'),
    path('action/<int:product_id>/<str:action>/', cart_action_view, name='cart_action')
]