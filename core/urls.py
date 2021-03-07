from django.urls import path
from .views import (
    item_list,
    ItemDetailView,
    CheckoutView,
    HomeView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView, name='home'),
    path('checkout/', CheckoutView, name='checkout'),
    path('product/', ItemDetailView, name='product')
]
