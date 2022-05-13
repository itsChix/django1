from django.contrib import admin
from .models import Meeting, Location, Participant
# Register your models here.
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("title", "address")
    list_filter = ("title", )
    prepopulated_fields = {"address": ("title", )}

admin.site.register(Meeting)
admin.site.register(Location)
admin.site.register(Participant)

