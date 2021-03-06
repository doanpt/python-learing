from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


@admin.register(User)
class ProfileUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'full_name', 'year_birth', 'about')
