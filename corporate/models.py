from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.deletion import CASCADE


# Create your models here.

class Property(models.Model):
    pproperty_image= models.FileField(upload_to='property_image')
    property_type=models.CharField(max_length=255)
    full_property_price=models.FloatField(default=0.00)
    standard_price=models.FloatField(default=0.00)
    deluxe_room_price = models.FloatField(default=0.00)
    deluxe_room_with_patio_price = models.FloatField(default=0.00)
    property_address=models.CharField(max_length=255)
    description = RichTextField()
    whats_near_by = RichTextField()
    property_size = models.CharField(max_length=255)
    no_of_garages = models.PositiveBigIntegerField(default=0)
    no_of_rooms = models.PositiveBigIntegerField(default=0)
    no_of_bathrooms = models.PositiveBigIntegerField(default=0)
    no_of_bedrooms = models.PositiveBigIntegerField(default=0)
    youtube_link =models.URLField(blank=True,null=True)
    slug = models.SlugField(unique=True)
    agent = models.ForeignKey('Agent',related_name="property_agent",on_delete=CASCADE)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.property_type + " ("+self.property_address+")"


    class Meta:
        ordering = ["timestamp",]
        verbose_name_plural = "properties"

class Amenity(models.Model):
    property = models.ForeignKey(Property,related_name="property_anemity",on_delete=CASCADE)
    name = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.property.property_type

    class Meta:
        ordering = ["timestamp",]
        verbose_name_plural = "Anemities"

class PropertyImage(models.Model):
    property = models.ForeignKey(Property,related_name="property_image",on_delete=CASCADE)
    property_gallery_image= models.FileField(upload_to='property_gallery_image')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.property.property_type


    class Meta:
        ordering = ["timestamp",]

class Slider(models.Model):
    background_image= models.FileField(upload_to='background_image')
    text1=models.CharField(max_length=255)
    text2=models.CharField(max_length=255)
    text3=models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text1


    class Meta:
        ordering = ["timestamp",]     

class Agent(models.Model):
    image= models.FileField(upload_to='agent_image')
    full_name=models.CharField(max_length=255)
    position=models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    description = RichTextField()
    linkedin = models.CharField(max_length=255,blank=True,null=True)
    facebook = models.URLField(max_length=255,blank=True,null=True)
    twitter = models.URLField(max_length=255,blank=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name_plural = "Hosts"


    class Meta:
        ordering = ["timestamp",]

class BookingIdTracker(models.Model):
    name = models.CharField(max_length=255)
    booking_id = models.PositiveBigIntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.booking_id


    class Meta:
        ordering = ["timestamp",]

class CustomerInfo(models.Model):
    full_name = models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    address = models.TextField()
    phone_number=models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name +" - "+ self.email


    class Meta:
        ordering = ["timestamp",]

class Booking(models.Model):
    BOOKING_STATUS = (
        ('active','Active'),
        ('checked in','Checked In'),
        ('cancelled','Cancelled'),
        ('checked out','checked out'),
    )
    property = models.ForeignKey(Property,related_name="property_booking",on_delete=CASCADE)
    customer = models.ForeignKey(CustomerInfo,related_name="info_booking_customer",on_delete=CASCADE)
    booking_id = models.CharField(max_length=255)
    booking_status = models.CharField(max_length=100, choices=BOOKING_STATUS,default='active')
    booking_options = models.CharField(max_length=255)
    date=models.CharField(max_length=255)
    children=models.CharField(max_length=255)
    adults=models.CharField(max_length=255)
    total_cost = models.FloatField(default=0.00)
    number_of_people = models.CharField(max_length=255)
    number_of_days = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.booking_id + " " + self.customer.email


    class Meta:
        ordering = ["timestamp",]

class CheckOutCustomer(models.Model):
    property = models.ForeignKey(Property,related_name="checkout_property",on_delete=CASCADE)
    notes = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.property.property_address


    class Meta:
        ordering = ["timestamp",]

class GeneralPage(models.Model):
    CHOICES = (
        ('','Choose page name'),
        ('terms-and-conditions','Terms & Conditions'),
        ('about-us','About Us'),
    )
    name = models.CharField(max_length=255, choices=CHOICES)
    description = RichTextField()
    slug = models.SlugField(unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


    class Meta:
        ordering = ["timestamp",]



