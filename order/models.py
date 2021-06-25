from django.db import models

from cart.models import Cart
from user.models import CustomerUser


class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255, default='')
    order_description = models.CharField(max_length=255, default='')
    order_total = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
