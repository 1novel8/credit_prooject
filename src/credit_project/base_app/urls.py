from django.urls import path, include
from .views import router, query

urlpatterns = [
    path('', (include(router.urls))),
    path('query/<int:pk>/', query),
]
