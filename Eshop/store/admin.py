from django.contrib import admin
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.product import Products

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Products)

# admin 123