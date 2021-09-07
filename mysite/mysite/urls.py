from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('inspections/',include('inspections.urls')),
    path('admin/', admin.site.urls),
]
