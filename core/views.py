from django.shortcuts import render
from .models import Item, OrderItem, Order

def item_list(request):
    context = {
        'items': Item.objects.all()

    }
    return render(request, "base.html", context)

def HomeView(request):
    return render(request, "base.html")

def ItemDetailView(request):
    return render(request, "product-page.html")

def CheckoutView(request):
    return render(request, "checkout-page.html")
