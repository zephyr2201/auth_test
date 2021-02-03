from django.contrib import admin
from django.urls import path
from . views import CustomAuth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', CustomAuth.as_view())
]
