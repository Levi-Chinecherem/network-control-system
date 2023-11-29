# congestion_control_app/views.py
import random
import threading
import time
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse
from .models import NetworkDevice, PerformanceData

def home(request):
    return render(request, 'congestion_control_app/home.html')

@login_required
def network_device_list(request):
    devices = NetworkDevice.objects.filter(user=request.user)
    return render(request, 'congestion_control_app/network_device_list.html', {'devices': devices})

@login_required
def add_network_device(request):
    if request.method == 'POST':
        name = request.POST['name']
        status = request.POST['status']
        quantity = int(request.POST['quantity'])

        selected_device = next(device for device in NetworkDevice.DEVICE_CHOICES if device[0] == name)
        unique_network_rate = float(selected_device[1].split('-')[1].strip())

        final_rate = unique_network_rate * quantity

        new_device = NetworkDevice.objects.create(user=request.user, name=name, status=status, quantity=quantity, final_rate=final_rate)
        
        messages.success(request, 'Network device added successfully.')

        initial_cpu_usage = random.uniform(1, 10)
        initial_memory_usage = random.uniform(1, 10)

        PerformanceData.objects.create(device=new_device, cpu_usage=initial_cpu_usage, memory_usage=initial_memory_usage)

        return redirect('network_device_list')
    
    device_choices = [(choice[0], choice[1].split('-')[0].strip()) for choice in NetworkDevice.DEVICE_CHOICES]
    status_choices = NetworkDevice.STATUS_CHOICES

    devices = NetworkDevice.objects.filter(user=request.user)
    return render(
        request,
        'congestion_control_app/add_network_device.html',
        {'devices': devices, 'device_choices': device_choices, 'status_choices': status_choices}
    )

@login_required
def update_network_device(request, device_id):
    device = get_object_or_404(NetworkDevice, pk=device_id, user=request.user)

    if request.method == 'POST':
        device.name = request.POST['name']
        device.status = request.POST['status']
        device.quantity = request.POST['quantity']
        device.save()
        messages.success(request, 'Network device updated successfully.')
        return redirect('network_device_list')

    return render(request, 'congestion_control_app/update_network_device.html', {'device': device})

@login_required
def delete_network_device(request, device_id):
    device = get_object_or_404(NetworkDevice, pk=device_id, user=request.user)
    device.delete()
    messages.success(request, 'Network device deleted successfully.')
    return redirect('network_device_list')

def update_performance_data():
    while True:
        performance_data_instances = PerformanceData.objects.filter(device__status='operational')

        for performance_data in performance_data_instances:
            current_time = timezone.now()
            elapsed_seconds = (current_time - performance_data.timestamp).total_seconds()
            rate_increase = 0.03  # 3% increase every 4 seconds

            new_cpu_usage = performance_data.cpu_usage + (
                performance_data.device.final_rate * rate_increase * elapsed_seconds
            )
            new_memory_usage = performance_data.memory_usage + (
                performance_data.device.final_rate * rate_increase * elapsed_seconds
            )

            performance_data.cpu_usage = min(new_cpu_usage, 1000000.0)
            performance_data.memory_usage = min(new_memory_usage, 1000000.0)
            performance_data.timestamp = current_time
            performance_data.save()

        time.sleep(4)

@login_required
def system_dashboard(request):
    devices = NetworkDevice.objects.filter(user=request.user)
    performance_data = PerformanceData.objects.filter(device__user=request.user)

    # Convert performance_data to a list of dictionaries
    performance_data_list = [
        {
            'device_name': data.device.name,
            'timestamp': data.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'cpu_usage': data.cpu_usage,
            'memory_usage': data.memory_usage,
        }
        for data in performance_data
    ]

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse({'devices': list(devices.values()), 'performance_data': performance_data_list})
    else:
        # If it's not an AJAX request, render the HTML template

        # Start the update in a separate thread (non-blocking)
        threading.Thread(target=update_performance_data, daemon=True).start()

        return render(request, 'congestion_control_app/system_dashboard.html')
