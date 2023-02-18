import stripe
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.shortcuts import render,get_object_or_404,redirect
from airbnb.utils import generate_booking_id, number_of_days, number_of_people, total_cost
from .models import Property, Booking, CustomerInfo
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import models
from blog.models import NewsAndBlog

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    template_name='home.html'
    properties_qs = models.Property.objects.all()
    slider_qs = models.Slider.objects.all()[:1]
    agencies_qs = models.Agent.objects.all()
    news_and_blog_qs = NewsAndBlog.objects.all()[:4]
    context={
        'properties_qs':properties_qs,
        'slider_qs':slider_qs,
        'agencies_qs':agencies_qs,
        'news_and_blog_qs':news_and_blog_qs
    }
    return render(request,template_name,context)


def properties(request):
    template_name='properties.html'
    properties_qs = models.Property.objects.all()
    context={
        'properties_qs':properties_qs
    }
    return render(request,template_name,context)

def property_details(request,slug):
    template_name='property_details.html'
    obj =get_object_or_404( models.Property,slug=slug)
    return render(request,template_name,{'obj':obj})

def create_booking(request,property_id):
    if request.method == 'POST':
        qs = get_object_or_404(Property,id=property_id)
        children = request.POST.get('children')
        adults = request.POST.get('adult')
        booking_dates = request.POST.get('booking_date')
        generated_booking_id = generate_booking_id()
        created_customer = CustomerInfo.objects.create(
            address = request.POST.get('address'),
            full_name = request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone_number')
        )
        customer = get_object_or_404(CustomerInfo,id=created_customer.id)
        new_booking = Booking.objects.create(
            property = qs,
            customer = customer,
            booking_id = generated_booking_id,
            date = booking_dates.strip(),
            children = children,
            total_cost = total_cost(booking_dates, property_id),
            number_of_people = number_of_people(children,adults),
            number_of_days = number_of_days(booking_dates),
            slug = generated_booking_id,
            adults = adults
        )

    return redirect('corporate:customer_booking_summary',new_booking.booking_id)


def cancel_booking(request,booking_id):
    qs =get_object_or_404(Booking,booking_id=booking_id)
    qs.booking_status = 'cancelled'
    qs.save()
    messages.success(request, 'booking successfully cancelled.')
    return redirect('corporate:customer_booking_summary',booking_id) 


def my_booking(request):
    template_name='my_booking.html'
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        email = request.POST.get('email')
        does_exist = Booking.objects.filter(booking_id=booking_id,customer__email = email).first()
        if does_exist:
            request.session['booking_id'] = booking_id
            messages.success(request, "Successfully logged in")
            return redirect('corporate:customer_booking_summary',booking_id)
        else:
            messages.error(request,'Booking ID or email does not exist') 
    return render(request,template_name)

def logout(request):
    del request.session['booking_id']
    messages.success(request, "Successfully logged out")
    return redirect('corporate:my_booking')

def bookings(request):
    template_name='bookings.html'
    qs = Booking.objects.all()
    return render(request,template_name,{'obj':qs})

def create_booking_view(request):
    template_name='create_bookings.html'
    qs = Property.objects.all()
    return render(request,template_name,{'obj':qs})


def edit_status_view(request,booking_id):
    template_name='edit_status_view.html'
    qs = get_object_or_404(Booking, booking_id=booking_id)
    # print(qs.get_booking_status_display())
    choices = qs.BOOKING_STATUS
    print(choices)
    if request.method == 'POST':
        qs.booking_status = request.POST.get('booking')
        qs.save()
        messages.success(request,'Status successfully updates')
        return redirect('corporate:customer_booking_summary',booking_id)
    return render(request,template_name,{'obj':qs,'choices':choices,})

def customer_booking_summary(request,booking_id):
    template_name='customer_booking_summary.html'
    qs =get_object_or_404(Booking,booking_id=booking_id)
    return render(request,template_name,{'obj':qs}) 
# Stripe Integration
def create_checkout_session_view(request,booking_id):
    booking_info = get_object_or_404(Booking,booking_id=booking_id)
    
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
            'currency': 'ZAR',
            'product_data': {
            'name': booking_info.property.property_address,
            },
            'unit_amount': 10000,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=settings.DOMAIN + '/success',
        cancel_url=settings.DOMAIN + '/cancel',
        )
    return redirect(checkout_session.url)

def payment_checkout(request,booking_id):
    template_name = 'stripe/payment_checkout.html'  
    booking_info = get_object_or_404(Booking,booking_id=booking_id)
    context = {
        'STRIPE_PUBLIC_KEY' :  settings.STRIPE_PUBLIC_KEY,
        'obj':booking_info
    }
    return render(request,template_name,context)


def success(request):
    template_name = 'stripe/success.html'
    return render(request,template_name)


def cancel(request):
    template_name = 'stripe/cancel.html'
    return render(request,template_name)

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        print(session)

        # todo decide whether you want to send the file or the URL
    
    elif event["type"] == "payment_intent.succeeded":
        intent = event['data']['object']

        stripe_customer_id = intent["customer"]
        stripe_customer = stripe.Customer.retrieve(stripe_customer_id)

        # customer_email = stripe_customer['email']
        # product_id = intent["metadata"]["product_id"]
    return HttpResponse(status=200)

def general_page(request,page_name):
    template_name = 'general_page.html'
    qs = get_object_or_404(models.GeneralPage, name=page_name)
    return render(request, template_name,{'obj':qs})

def contact(request):
    template_name = 'contact.html'
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        to = settings.TO_
        email_user = settings.EMAIL_USER
        message = MIMEMultipart("alternative")
        message["Subject"] = name + ' '+ lastname
        message["From"] = email_user
        message["To"] = to
        body = """\
            <html>
            <head> </head>
            <body>
                <h4>Website Email</h4>
                <p>%s</p>
                <p>received from: %s - (%s)</p>
            </body>
            </html>
            """ % (request.POST.get('message'),email,name + ' '+lastname)
        message.attach(MIMEText(body, "html"))
        try:
            print('we are here')
            smtp_server = smtplib.SMTP_SSL(settings.SMTP, settings.PORT)
            print(smtp_server)
            smtp_server.ehlo()
            smtp_server.login(email_user,settings.PASSWORD)
            smtp_server.sendmail(email_user, to, message.as_string())
            smtp_server.close()
            messages.success(request, 'Request successfully sent we will contact you soon.')
        except Exception as ex:
            print ("Something went wrong….",ex)
            messages.error(request,'Something went wrong.')    
    return render(request, template_name)

        