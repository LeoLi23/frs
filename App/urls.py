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
    path('customer/logout/', views.logout_customer, name='logout_customer'),
    path('customer/search/', views.customer_search, name='customer_search'),
    path('customer/search/purchase', views.customer_purchase, name='customer_purchase'),
    path('customer/comment', views.customer_comment, name='customer_comment'),
    path('customer/myspending/', views.customer_spending, name='customer_spending'),

    path('staff/register/', views.register_staff, name='register_staff'),
    path('staff/login/', views.login_staff, name='login_staff'),
    path('staff/logout/', views.logout_staff, name='logout_staff'),
    path('staff/view_customers/', views.view_customers_staff, name='view_customers_staff'),
    path('staff/create_flight/', views.create_flight_staff, name='create_flight_staff'),
    path('staff/changeStatus', views.change_flight_status, name='change_flight_status'),
    path('staff/add_airplane/', views.add_airplane_staff, name='add_airplane_staff'),
    path('staff/add_airport/', views.add_airport_staff, name='add_airport_staff'),
    path('staff/view_ratings', views.view_flight_ratings, name='view_ratings_staff'),
    path('staff/view_frequent_customers/', views.view_most_frequent_customers, name='view_most_frequent_customers'),
    path('staff/view_frequent_customers/view_flights_for_one_customer', views.view_flights_for_one_customer,
         name='view_flights_for_one_customer'),
    path('staff/view_reports', views.view_reports_staff, name='view_reports_staff'),

    path('booking_agent/register/', views.register_booking_agent, name='register_booking_agent'),
    path('booking_agent/login/', views.login_booking_agent, name='login_booking_agent'),

]
