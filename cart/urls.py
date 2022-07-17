from django import urls
from django.urls import path
from .views import *

app_name = 'cart'


urlpatterns = [
    path('order-summary/', OrderSummary, name='order-summary'),
    path('add-to-cart/<int:pk>', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<int:pk>', remove_from_cart, name="remove-from-cart"),
    path("reduce_quantity_item/<int:pk>",
         remove_single_item_from_cart, name="reduce-quantity-item"),
    path('PlaceOrder/',PlaceOrder, name='PlaceOrder'),
    # path('payment/', PaymentView.as_view(), name='payment'),


]
