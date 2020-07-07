from django.contrib import admin
from .models import Action

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ("created","user", "verb","target",)
    search_fields = ("user","verb",)
    list_filter = ("created",)
