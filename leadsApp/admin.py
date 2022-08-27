from django.contrib import admin
from leadsApp.models import Lead

# Register your models here.
admin.site.register(Lead)


class LeadAdmin(admin.ModelAdmin):
    display_list = [all]
