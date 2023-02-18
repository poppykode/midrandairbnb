from rest_framework import serializers
from corporate.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('property','booking_id','date')