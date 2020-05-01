from django.urls import path
from .  import views


urlpatterns=[
    path('',views.index),
    path('offers',views.offers),
    path('wishlist',views.wishlist),
    path('transactions',views.transactions),
    path('My_orders',views.my_orders),
    path('filters',views.filters)
]