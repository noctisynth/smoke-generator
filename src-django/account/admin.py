from django.contrib import admin
from .models import UserAccount


# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("username", "phone", "email", "status")


admin.site.register(UserAccount, UserAccountAdmin)
