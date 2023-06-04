from django.contrib import admin
from django.urls import path, include

from base_app.urls import urlpatterns as baseapp_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(baseapp_urls))
]
