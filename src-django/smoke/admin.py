from django.contrib import admin
from .models import Record

# Register your models here.


class RecordAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "pic_type", "date")


admin.site.register(Record, RecordAdmin)
