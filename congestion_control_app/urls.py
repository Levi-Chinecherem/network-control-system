# congestion_control_app/urls.py
from django.urls import path
from .views import network_device_list, add_network_device, update_network_device, delete_network_device, system_dashboard, home

urlpatterns = [
    path('', home, name='home'),
    path('network_device_list/', network_device_list, name='network_device_list'),
    path('add_network_device/', add_network_device, name='add_network_device'),
    path('update_network_device/<int:device_id>/', update_network_device, name='update_network_device'),
    path('delete_network_device/<int:device_id>/', delete_network_device, name='delete_network_device'),
    path('system_dashboard/', system_dashboard, name='system_dashboard'),
]
