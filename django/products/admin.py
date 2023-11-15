"""
Admin configuration for products.
"""
from products.models import Product

from django.contrib import admin

admin.site.register(Product)
