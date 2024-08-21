"""
URL configuration for django_lab_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('/home', views.home_view, name='home'),
    path('/add_product', views.add_product_view, name='add_product'),
    path('/products', views.products, name='products'),
    path('/edit_products', views.edit_product_view, name='edit_products'),
    path('/delete', views.product_delete_method, name='delete'),
    path('/update', views.product_update_method, name='upadte')
]
