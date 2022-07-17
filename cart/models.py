from django.db import models
from django.contrib.auth.models import User
from gallery.models import painting

# Create your models here.


class Order(models.Model):
    """Model definition for CartItem."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(painting, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        """Meta definition for CartItem."""
        verbose_name_plural = 'Orders'

    def __str__(self):
        """Unicode representation of Orders."""
        return f"{self.quantity} of {self.item.flower_name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    # def get_discount_item_price(self):
    #     return self.quantity * self.item.discount_price

    # def get_amount_saved(self):
    #     return self.get_total_item_price() - self.get_discount_item_price()

    # def get_final_price(self):
    #     return self.get_total_item_price()


class CartItem(models.Model):
    """Model definition for CartItems."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Order)
    start_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField(null=True,blank=True)
    # order_address = models.ForeignKey(
    #     UserAddress, on_delete=models.SET_NULL, blank=True, null=True)
    ordered = models.BooleanField(default=False)

    class Meta:
        """Meta definition for CartItem."""

        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'

    def __str__(self):
        """Unicode representation of CartItem."""
        return self.user.username

    def get_total_price(self):
        total = 0
        for order_item in self.item.all():
            total += order_item.get_total_item_price()
        return total

    def get_final_price(self):
        return self.get_total_price() + 50

    # def get_amount_saved(self):
    #     total = 0
    #     for order_item in self.item.all():
    #         total += order_item.get_amount_saved()
    #     return total

    # def price_afted_saved(self):
    #     total = 0
    #     for order_item in self.item.all():
    #         total += order_item.get_final_price()
    #     return total
