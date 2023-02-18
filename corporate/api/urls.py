  
from django.urls import path
from .views import get_bookings
urlpatterns = [
    path('bookings/<int:property_id>', get_bookings),
]