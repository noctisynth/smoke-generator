from django.contrib import admin
from .models import PublicJoint, PublicSmoke

# Register your models here.


class PublicSmokeAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "username", "date")


class PublicJointAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "username", "date")


admin.site.register(PublicSmoke, PublicSmokeAdmin)
admin.site.register(PublicJoint, PublicJointAdmin)
