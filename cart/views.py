from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.views.generic import ListView, DetailView, View
from .models import Order, CartItem
from gallery.models import painting


@login_required(login_url='/login/')
def OrderSummary(request):
    cart_items,created = CartItem.objects.get_or_create(
        user=request.user, ordered=False)
    context = {'cart_items': cart_items}
    print(cart_items)
    return render(request, 'cart.html', context)



@login_required(login_url='/login/')
def add_to_cart(request, pk):
    item = get_object_or_404(painting, pk=pk)
    ordered_item, created = Order.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )

    user_cartitem = CartItem.objects.filter(
        user=request.user, ordered=False)

    if user_cartitem.exists():
        cart_item = user_cartitem[0]

        if cart_item.item.filter(item__pk=item.pk).exists():
            ordered_item.quantity += 1
            ordered_item.save()
            messages.success(request, "Added Quantity Item")
            return redirect("cart:order-summary")
        else:
            cart_item.item.add(ordered_item)
            messages.success(request, "Added Item to your cart")
            return redirect("cart:order-summary")

    else:
        ordered_date = timezone.now()
        cart_item = CartItem.objects.create(
            user=request.user, order_date=ordered_date)
        cart_item.item.add(ordered_item)
        messages.success(request, "Added Item to your cart")
        return redirect("cart:order-summary", pk=pk)


@login_required(login_url='/login/')
def remove_from_cart(request, pk):
    item = get_object_or_404(painting,pk=pk)
    user_cartitems = CartItem.objects.filter(user=request.user,
                                             ordered=False
                                             )
    if user_cartitems.exists():
        cart_items = user_cartitems[0]

        if cart_items.item.filter(item__pk=item.pk).exists():
            order_item = Order.objects.filter(user=request.user,
                                              item=item,
                                              ordered=False)[0]
            order_item.delete()
            messages.success(request, "Item \"" +
                             order_item.item.Title+"\" removed from your cart")
            return redirect("cart:order-summary")
        else:
            messages.success(request, "This Item not in your cart")
            return redirect("cart:order-summary")
    else:
        messages.success(request, "You do not have an Order")
        return redirect("cart:order-summary")


@login_required(login_url='/login/')
def remove_single_item_from_cart(request, pk):
    item = get_object_or_404(painting,pk=pk)
    user_cartitems = CartItem.objects.filter(user=request.user,
                                             ordered=False
                                             )
    if user_cartitems.exists():
        cart_items = user_cartitems[0]

        if cart_items.item.filter(item__pk=item.pk).exists():
            order_item = Order.objects.filter(user=request.user,
                                              item=item,
                                              ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.success(request, "Cart Updated")
            return redirect("cart:order-summary")

        else:
            messages.success(request, "This Item is not in your cart")
            return redirect("cart:order-summary")
    else:
        messages.success(request, "You do not have an Order")
        return redirect("cart:order-summary")

@login_required(login_url='/login/')
def PlaceOrder(request):
    cart_items = CartItem.objects.get(user=request.user, ordered=False)
    # order = Order.objects.filter(user=request.user, ordered=False)


    order_items = cart_items.item.all()
    order_items.update(ordered=True)
    for item in order_items:
        item.save()

    cart_items.ordered = True
    cart_items.save()
    messages.success(request, "Your Order has been placed")
    return redirect("/")