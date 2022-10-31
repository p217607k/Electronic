"""Electronic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.base,name='base_page'),
    path('',views.index,name='index_page'),
    path('product/',views.profile_view,name='profile_page'),
    path('product/<str:id>/',views.product_single_view,name='product_single_page'),
    path('search/',views.search_view,name='search_page'),
    path('contect/',views.contect_view,name='contect_page'),
    #### contect
    path('registrations/',views.authentication_view,name='authentication_page'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    ##### cart
    
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('checkout/', views.checkout_view, name='checkout_page'),
  #### payment
    path('order/',views.order_view,name='payment_page'),
    ### thankyou
    path('success/',views.thankyou_view,name='thankyou_page'),
    path('yourorder/',views.yourorder_view,name='yourorder_page'),
    










]