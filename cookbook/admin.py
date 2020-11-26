from django.contrib import admin

from cookbook.models import Ingredient, Category

admin.site.register(Category)
admin.site.register(Ingredient)