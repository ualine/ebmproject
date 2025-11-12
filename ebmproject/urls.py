# ebmproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # ⚙️ Admin interface
    path('admin/', admin.site.urls),

    # 🌐 Include all routes from the 'sales' app
    path('', include('sales.urls')),
]
