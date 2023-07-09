from django.contrib import admin
from ..models import *
from .supplier_card import SupCardAdmin
from .category import CategoryAdmin
from .product import ProductAdmin


admin.site.register(Category, CategoryAdmin)
admin.site.register(SupplierCard, SupCardAdmin)
admin.site.register(Product, ProductAdmin)