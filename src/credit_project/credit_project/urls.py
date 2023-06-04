from django.contrib import admin
from django.urls import path, include

from base_app.urls import urlpatterns as baseapp_urls


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(baseapp_urls))
]
