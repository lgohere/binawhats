from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recebezap/', include('recebezap.urls', namespace='recebezap')),
]
