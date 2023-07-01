"""
URL configuration for Selector project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name = "home"),

    path('add_supplier_card', views.add_supplier_card, name = "add_supplier_card"),

    path('add_category', views.add_category, name='add_category'),

    path('categories', views.category_list, name='category_list'),

    path('suppliers', views.supplier_card_list, name='supplier_card_list')
    #
    # path('supplier_card/<str:supplier_card_id>', views.supplier_card, name = "add_supplier_card"),
    #
    # path('edit_supplier_card', views.edit_supplier_card, name = "edit_supplier_card"),
    #
    # path('delete_supplier_card', views.delete_supplier_card, name = "delete_supplier_card")
]
