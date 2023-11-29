import random
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class NetworkDevice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    DEVICE_CHOICES = [
        ('router1', 'Router 1 - 10.0'),
        ('switch1', 'Switch 1 - 15.0'),
        ('server1', 'Server 1 - 20.0'),
        ('computer1', 'Computer 1 - 5.0'),
        ('printer1', 'Printer 1 - 8.0'),
        ('access_point1', 'Access Point 1 - 12.0'),
        ('firewall1', 'Firewall 1 - 18.0'),
        ('modem1', 'Modem 1 - 25.0'),
        ('storage1', 'Storage 1 - 30.0'),
        ('camera1', 'Camera 1 - 7.0'),
        ('phone1', 'Phone 1 - 3.0'),
        ('tablet1', 'Tablet 1 - 9.0'),
        ('laptop1', 'Laptop 1 - 14.0'),
        ('smart_tv1', 'Smart TV 1 - 22.0'),
        ('iot_device1', 'IoT Device 1 - 17.0'),
    ]

    STATUS_CHOICES = [
        ('operational', 'Operational'),
        ('maintenance', 'Maintenance'),
        ('offline', 'Offline'),
        ('error', 'Error'),
    ]

    name = models.CharField(max_length=50, choices=DEVICE_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    quantity = models.IntegerField(default=1)
    final_rate = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.get_name_display()


class PerformanceData(models.Model):
    device = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    cpu_usage = models.FloatField()
    memory_usage = models.FloatField()

    def __str__(self):
        return f"{self.device.name} - {self.timestamp}"
