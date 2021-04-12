from django.urls import path
from . import views

app_name = 'App'  # specify the app name
urlpatterns = [
    path('', views.info, name='main'),

    path('customer/', views.customer_index, name='customer_index'),
    path('staff/', views.staff_index, name='staff_index'),
    path('booking_agent/', views.agent_index, name='agent_index'),

    path('customer/register/', views.register_customer, name='register_customer'),
    path('customer/login/', views.login_customer, name='login_customer'),

    path('staff/register/', views.register_staff, name='register_staff'),
    path('staff/login/', views.login_staff, name='login_staff'),

    path('booking_agent/register/', views.register_booking_agent, name='register_booking_agent'),
    path('booking_agent/login/', views.login_booking_agent, name='login_booking_agent'),

    path('customer/search/', views.customer_search, name='customer_search'),
    path('customer/search/purchase', views.customer_purchase, name='customer_purchase'),
]
