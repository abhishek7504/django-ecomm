from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","phone_number","email",)
    list_filter = ("staff","admin","active",)
    search_fields = ("phone_number", )
    readonly_fields = ("password", )


    