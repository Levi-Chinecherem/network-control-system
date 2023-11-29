# congestion_control_app/admin.py
from django.contrib import admin
from .models import NetworkDevice, PerformanceData

class NetworkDeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'final_rate', 'user')
    search_fields = ('name', 'status')
    list_filter = ('status', 'user')

class PerformanceDataAdmin(admin.ModelAdmin):
    list_display = ('device', 'timestamp', 'cpu_usage', 'memory_usage')
    search_fields = ('device__name',)
    list_filter = ('device__status',)

admin.site.site_header = "Congestion Control Admin"
admin.site.site_title = "Congestion Control Admin"
admin.site.index_title = "Welcome to the Congestion Control Admin"

admin.site.register(NetworkDevice, NetworkDeviceAdmin)
admin.site.register(PerformanceData, PerformanceDataAdmin)
