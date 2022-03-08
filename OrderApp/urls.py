from django.urls import path
from .import views

urlpatterns = [
    path('addingcart/<int:id>/', views.Add_to_Shoping_cart, name='Add_to_Shoping_cart'),
    path('cart_details/', views.cart_details, name='cart_details'),


]