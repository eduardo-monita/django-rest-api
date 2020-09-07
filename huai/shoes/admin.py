from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Vendedor

@admin.register(Vendedor)
class CustomUserAdmin(UserAdmin):
    model = Vendedor

# Register your models here.