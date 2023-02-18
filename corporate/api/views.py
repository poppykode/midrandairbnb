from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK ,HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import BookingSerializer
from corporate.models import Booking, Property
import json

@api_view(['GET'])
def get_bookings(request,property_id):
    if request.method =='GET':
        property = get_object_or_404(Property,id=property_id)
        qs = Booking.objects.filter(property=property).exclude(booking_status ='cancelled').exclude(booking_status='checked out')
        dates = ""
        for booking in qs:
            dates+= booking.date.strip().replace('/','-') + ","
        data = list(dates.split(","))
        while("" in data):
            data.remove("")
        print(data)
        return Response(data,status=HTTP_200_OK)
    return Response(status=HTTP_400_BAD_REQUEST)



