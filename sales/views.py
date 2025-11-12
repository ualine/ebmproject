from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
import json

# 🖥️ 1️⃣ DASHBOARD VIEW
def dashboard(request):
    """
    Renders the main IoT dashboard interface.
    """
    return render(request, 'sales/dashboard.html')


# 🌡️ 2️⃣ SIMULATED SENSOR DATA (for chart testing)
def sensor_data(request):
    """
    Simulates random IoT sensor readings for the dashboard charts.
    This is mainly for front-end testing before connecting real IoT devices.
    """
    data = {
        'temperature': round(random.uniform(25, 30), 2),
        'humidity': round(random.uniform(60, 70), 2),
        'co2': random.randint(700, 800),
        'dust': round(random.uniform(2, 4), 2),
        'ammonia': random.randint(10, 15),
    }
    return JsonResponse(data)


# 📡 3️⃣ REAL IOT DATA RECEIVER (from ESP32 / Pico W)
@csrf_exempt
def receive_data(request):
    """
    Receives real IoT sensor data sent from a microcontroller via HTTP POST.
    Example JSON payload:
    {
        "temperature": 27.5,
        "humidity": 65,
        "co2": 780,
        "dust": 2.3,
        "ammonia": 11
    }
    """
    if request.method == "POST":
        try:
            # Parse incoming JSON data
            data = json.loads(request.body)

            # Extract each field
            temperature = data.get("temperature")
            humidity = data.get("humidity")
            co2 = data.get("co2")
            dust = data.get("dust")
            ammonia = data.get("ammonia")

            # Print to terminal for now (later, we’ll save to DB)
            print("\n📩 Received IoT Data:")
            print(f"🌡 Temperature: {temperature} °C")
            print(f"💧 Humidity: {humidity} %")
            print(f"🫧 CO₂: {co2} ppm")
            print(f"🌫 Dust: {dust} µg/m³")
            print(f"☠️ Ammonia: {ammonia} ppm\n")

            # Return confirmation to device
            return JsonResponse({"message": "Data received successfully!"})

        except Exception as e:
            # Return error if JSON or data structure is invalid
            return JsonResponse({"error": str(e)}, status=400)

    # If method is GET, just show info
    return JsonResponse({"message": "Send data using POST method"})
