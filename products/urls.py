"""ecommerce_old URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:cat_id>', views.products, name='products'),
    path('product/<int:prod_id>', views.product, name='product'),
    path('search', views.search, name='search'),
    path('add', views.add, name='add'),
    path('delete/<int:prod_id>', views.delete, name='delete'),
    path('cart', views.cart, name='cart'),
    path('pay', views.pay, name='pay'),
]
