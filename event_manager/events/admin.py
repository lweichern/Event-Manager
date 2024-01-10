from django.contrib import admin
from .models import Events

# Register your models here.
class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "created_by", "created_date", "updated_date", "tasksNotDone")
    ordering = ("id",)

admin.site.register(Events, EventsAdmin)