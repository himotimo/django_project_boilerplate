from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.utils import timezone
from .models import Item, OrderItem, Order

def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home.html", context)


def CheckoutView(request):
    return render(request, "checkout-page.html")

class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = "home.html"

class SearchPageView(ListView):
    model = Item
    paginate_by = 10
    template_name = "home.html"

    def get_queryset(self):
        query = self.request.GET.get('query')
        return Item.objects.filter(title__icontains=query)

class OrderedPageView(ListView):
    model = Item
    paginate_by = 10
    template_name = "home.html"

    def get_queryset(self):
        s = self.request.GET.get('price_filter')
        if s=='1':
            return Item.objects.order_by('price')
        elif s=='2':
            return Item.objects.order_by('-price')
        return Item.objects.all()


class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"

class ShoppingCartView(ListView):
    model = Item
    template_name = "cart.html"

def add_to_cart(request, slug):
    item = get_object_or_404(Item,slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered= False
    )
    order_qs = Order.objects.filter(user=request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request, "This item quantity was updated.")

        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart")
            return redirect("core:product",slug= slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user= request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
        return redirect("core:product",slug= slug)

def remove_from_cart(request, slug):
    item = get_object_or_404(Item,slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered= False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart")
            return redirect("core:product", slug=slug)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You don't have an order yet.")
        return redirect("core:product",slug= slug)
