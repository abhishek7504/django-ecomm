from django.urls import path
from .import views

app_name = 'web'

urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('search/',views.search,name='search'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('detail/<int:pk>/',views.product_detial,name='product_detial'),
    path('add-wishlist/<int:pk>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('remove-product/<int:pk>/',views.remove_from_wishlist,name='remove_from_wishlist'),

]