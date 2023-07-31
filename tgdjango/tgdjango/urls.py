from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('tgdjango.app.urls')),
    path('admin/', admin.site.urls),
]
