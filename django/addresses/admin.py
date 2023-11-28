"""
Admin configuration for employees.
"""

from addresses.models import Address

from django.contrib import admin

admin.site.register(Address)
