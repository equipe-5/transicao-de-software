from django.contrib import admin

# Register your models here.
"""
Admin configuration for products.
"""
from users.models import User

from django.contrib import admin

admin.site.register(User)
