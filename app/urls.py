from django.urls import path
from .views import landgingview

urlpatterns = [
    path('', landgingview),
]
