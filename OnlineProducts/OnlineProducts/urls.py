"""OnlineProducts URL Configuration

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
from django.urls import path
from OnlineProducts import views
from .views import update_product

urlpatterns = [
    path('', views.product_list),
    path('products/', views.product_list),
    path('products/<int:id>', views.product_detail),
    path('create/', views.create_product),
    path('update/<int:id>', views.update_product),
    path('delete/<int:id>', views.delete_product)
]
