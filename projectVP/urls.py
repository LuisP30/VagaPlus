from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('plans.urls')) # O include está incluindo as URL's de sua URL filha: URLS-plans
]