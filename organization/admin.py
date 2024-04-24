from django.contrib import admin
from .models import Organization, Profile

# Register your models here.

# class OrganizationAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'domain', 'year_founded', 'industry', 'size_range', 'locality', 'country', 'linkedin_url', 'current_employee_estimate', 'total_employee_estimate']

admin.site.register(Organization)
admin.site.register(Profile)
