from django.contrib import admin
from hostinfo.models import Host

# Register your models here.
class HostAdmin(admin.ModelAdmin):
    list_display = ['hostname',
                    'ip',
                    'cpu_model',
                    'cpu_num',
                    'memory',
                    'osver',
                    'vendor',
                    'product',
                    'sn']


admin.site.register(Host, HostAdmin)


