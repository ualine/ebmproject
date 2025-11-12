# sales/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 🖥️ Dashboard main page
    path('', views.dashboard, name='dashboard'),

    # 🔄 Simulated IoT sensor data (for dashboard charts)
    path('api/data/', views.sensor_data, name='sensor_data'),

    # 📡 Real IoT data endpoint (for ESP32 or Pico W)
    path('api/send/', views.receive_data, name='receive_data'),
]
