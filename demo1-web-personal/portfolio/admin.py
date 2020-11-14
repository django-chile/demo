from django.contrib import admin
from .models import Project

# Register your models here.
class ProjecAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Project, ProjecAdmin)
