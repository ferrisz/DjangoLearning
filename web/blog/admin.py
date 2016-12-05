from django.contrib import admin

# Register your models here.

from blog.models import Host

class HostAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'ip']

admin.site.register(Host, HostAdmin)