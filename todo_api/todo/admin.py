from django.contrib import admin

# Register your models here.
from .models import Todo, Item

admin.site.register(Todo)
admin.site.register(Item)