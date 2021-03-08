from django.urls import path
from .views import (
    item_list,
    ItemDetailView,
    CheckoutView,
    HomeView,
    add_to_cart,
    remove_from_cart,
    SearchPageView,
    OrderedPageView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView, name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/',add_to_cart,name='add-to-cart'),
    path('remove-from-cart/<slug>/',remove_from_cart,name='remove-from-cart'),
    path('search/',SearchPageView.as_view(),name="search-results"),
    path('order/',OrderedPageView.as_view(),name="order-results")
]
