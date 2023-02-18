import datetime
from corporate.models import BookingIdTracker, Property
from django.shortcuts import get_object_or_404

def generate_booking_id():
    obj, created = BookingIdTracker.objects.get_or_create(name="booking",defaults={'booking_id': 0},)
    id_=0
    if obj:
        id_=obj.booking_id + 1
        obj.booking_id = id_
        obj.save()
    if created:
        id_ = 1
    year  = str(datetime.date.today().year)
    booking_id = 'MIDABNB'+ year + str(id_)
    return booking_id

def number_of_people(a,c):
    total = int(a) + int(c)
    return str(total)
    
def total_cost(dates, property_id):
    n = number_of_days(dates)
    qs = get_object_or_404(Property,id=property_id)
    total = (qs.property_price * n)
    return total

def number_of_days(dates):
    data = list(dates.split(","))
    return len(data)

