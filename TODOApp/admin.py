from django.contrib import admin
from .models import TODO

@admin.register(TODO)
class TODO(admin.ModelAdmin):
    list_display = ['id','item']
