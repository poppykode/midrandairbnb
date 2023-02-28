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
    
def total_cost(dates, property_id,rooms):
    n = number_of_days(dates)
    qs = get_object_or_404(Property,id=property_id)
    sub_total = 0.0
    for room in rooms:                 
        if room =='Full House':
            sub_total += qs.full_property_price
            break
        elif room == 'Standard Room':
            sub_total += qs.standard_price
        elif room == 'Deluxe Room':
            sub_total += qs.deluxe_room_price
        elif room == 'Deluxe Room with Patio':
            sub_total += qs.deluxe_room_with_patio_price
        else:
            sub_total += qs.full_property_price
    total = (sub_total * n)
    return total

def number_of_days(dates):
    data = list(dates.split(","))
    return len(data)

