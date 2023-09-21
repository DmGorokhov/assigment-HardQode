from django.contrib import admin
from .models import SiteUser


# Register your models here.
@admin.register(SiteUser)
class SiteUserAdmin(admin.ModelAdmin):
    pass