from django.contrib import admin
from .models import SmokeRecord, JointRecord

# Register your models here.


class SmokeRecordAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "visible", "username", "date")


class JointRecordAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "visible", "username", "date")


admin.site.register(SmokeRecord, SmokeRecordAdmin)
admin.site.register(JointRecord, JointRecordAdmin)
