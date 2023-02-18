from django.urls import path
from . import views

app_name = 'corporate'
urlpatterns = [
    path('',views.home,name='home'),
    path('success', views.success,name='success'),
    path('cancel', views.cancel,name='cancel'),
    path('properties',views.properties,name='properties'),
    path('all/bookings',views.bookings,name='bookings'),
    path('logout/customer',views.logout,name='logout'),
    path('webhooks/stripe/', views.stripe_webhook, name='stripe_webhook'),
    path('payment/checkout/<str:booking_id>',views.payment_checkout,name='payment_checkout'),
    path('contact',views.contact,name='contact'),
    path('<str:page_name>',views.general_page,name='general_page'),
    path('details/<slug:slug>',views.property_details,name='property_details'),
    path('create-a-booking/<int:property_id>',views.create_booking,name='create_booking'),
    path('booking-cancellation/<str:booking_id>',views.cancel_booking,name='cancel_booking'),
    path('booking-summary/<str:booking_id>',views.customer_booking_summary,name='customer_booking_summary'),
    path('my-booking/account',views.my_booking,name='my_booking'),
    path('create-booking/view',views.create_booking_view,name='create_booking_view'),
    path('edit-status/view/<str:booking_id>',views.edit_status_view,name='edit_status_view'),
    path('create-checkout-session/<str:booking_id>',views.create_checkout_session_view,name='create_checkout_session_view'), 
]
