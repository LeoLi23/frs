from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import *
from django.urls import reverse
from App.utils import *
from django.db import connection
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
)


def info(request):
    if request.method == 'POST':
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            SourceCity = form.cleaned_data['SourceCity']
            DepartAirport = form.cleaned_data['DepartAirport']
            DestinationCity = form.cleaned_data['DestinationCity']
            ArriveAirport = form.cleaned_data['ArriveAirport']
            Depart_date = form.cleaned_data['Depart_date']
            Return_date = form.cleaned_data['Return_date']

            # one way trip
            if not Return_date:
                sql_str = "select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time " + \
                          "from flight,airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                          f" and flight.depart_airport_name = '{DepartAirport}' and D.city = '{SourceCity}' and " \
                          f"flight.arrive_airport_name = '{ArriveAirport}' and A.city = '{DestinationCity}' and depart_date = '{Depart_date}'"
                logging.info(sql_str)
                cursor = connection.cursor()
                cursor.execute(sql_str)
                flights = cursor.fetchall()
                cursor.close()
                connection.close()
                if flights:
                    print('one way flight search is successful')
                    return render(request, 'main.html', {'form': form,
                                                         'flights': flights,
                                                         'trip_count': 1})
                else:
                    print('cannot find flights')
                    return render(request, 'main.html', {'form': form,
                                                         'message': 'No flights available!'})

            # round trip
            else:
                sql_str1 = "select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time " + \
                           "from flight,airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                           f" and flight.depart_airport_name = '{DepartAirport}' and D.city = '{SourceCity}' and " \
                           f"flight.arrive_airport_name = '{ArriveAirport}' and A.city = '{DestinationCity}' and depart_date = '{Depart_date}'"

                sql_str2 = "select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time " + \
                           "from flight,airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                           f" and flight.depart_airport_name = '{ArriveAirport}' and D.city = '{DestinationCity}' and " \
                           f"flight.arrive_airport_name = '{DepartAirport}' and A.city = '{SourceCity}' and depart_date = '{Return_date}'"

                cursor = connection.cursor()

                cursor.execute(sql_str1)
                flight_first = cursor.fetchall()

                cursor.execute(sql_str2)
                flight_second = cursor.fetchall()

                cursor.close()
                connection.close()

                if flight_first and flight_second:
                    print("round trip flight search is successful")
                    return render(request, 'main.html', {'form': form,
                                                         'sourceCity': SourceCity,
                                                         'destinationCity': DestinationCity,
                                                         'flight_first': flight_first,
                                                         'flight_second': flight_second,
                                                         'trip_count': 2})
                else:
                    print('cannot find flights')
                    return render(request, 'main.html', {'form': form,
                                                         'message': 'No flights available!'})
    else:
        form = FlightSearchForm(request.POST)
    return render(request, 'main.html', {'form': form})


def agent_index(request):
    agent_email = request.session['user']
    agent = BookingAgent.objects.filter(agent_email__exact=agent_email).first()
    return render(request, 'booking_agent/index.html', {'agent': agent})


def staff_index(request):
    username = request.session['user']
    staff = Staff.objects.filter(username__exact=username).first()
    print(staff)
    return render(request, 'staff/index.html', {'staff': staff})


def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            password = form.cleaned_data['password2']
            building_num = form.cleaned_data['building_num']
            street = form.cleaned_data['street']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            phone_num = form.cleaned_data['phone_num']
            passport_num = form.cleaned_data['passport_num']
            passport_country = form.cleaned_data['passport_country']
            passport_expire = form.cleaned_data['passport_expire']
            date_of_birth = form.cleaned_data['date_of_birth']

            hashed_password = hashed(password)

            sql_str = f"insert into customer(email,name,password,building_num,street,city,state,phone_num,passport_num,passport_country,passport_expire,date_of_birth) " + \
                      f"values ('{email}','{name}','{hashed_password}','{building_num}','{street}','{city}','{state}','{phone_num}','{passport_num}','{passport_country}','{passport_expire}','{date_of_birth}')"
            print(sql_str)
            cursor = connection.cursor()
            cursor.execute(sql_str)
            cursor.close()
            connection.close()

            logging.info("Insertion is successful!")

            return HttpResponseRedirect(reverse('App:login_customer'))
    else:
        form = CustomerRegisterForm()
    return render(request, 'customer/register.html', {'form': form})


def register_staff(request):
    if request.method == 'POST':
        form = StaffRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            f_name = form.cleaned_data['f_name']
            l_name = form.cleaned_data['l_name']
            date_of_birth = form.cleaned_data['date_of_birth']

            airline_name = form.cleaned_data['airline_name']
            airline_instance = Airline.objects.get(airline_name__exact=airline_name)

            hashed_password = hashed(password)

            staff = Staff.objects.create(username=username, password=hashed_password,
                                         f_name=f_name, l_name=l_name,
                                         date_of_birth=date_of_birth, airline_name=airline_instance)

            staff.save()
            messages.success(request, f'Staff Account created for {username}!')
            return HttpResponseRedirect(reverse('App:login_staff'))
    else:
        form = StaffRegisterForm()
    return render(request, 'staff/register.html', {'form': form})


def register_booking_agent(request):
    if request.method == 'POST':
        form = BookingAgentRegisterForm(request.POST)
        if form.is_valid():
            agent_email = form.cleaned_data['agent_email']
            agent_id = form.cleaned_data['agent_id']
            agent_password = form.cleaned_data['password2']

            hashed_password = hashed(agent_password)

            booking_agent = BookingAgent.objects.create(agent_email=agent_email, agent_id=agent_id,
                                                        agent_password=hashed_password)

            booking_agent.save()
            messages.success(request, f'Booking agent Account created for {agent_email}')
            return HttpResponseRedirect(reverse('App:login_booking_agent'))
    else:
        form = BookingAgentRegisterForm()
    return render(request, 'booking_agent/register.html', {'form': form})


def login_customer(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            hashed_password = hashed(password)

            cursor = connection.cursor()
            cursor.execute(f"select email from customer where email = '{email}'")

            check_email = cursor.fetchall()
            if not check_email:
                return render(request, 'customer/login.html',
                              {'form': form, 'message': "Email address doesn't exist!", 'need_to_signup': True})

            cursor.execute(f"select email from customer where email = '{email}' and password = '{hashed_password}' ")
            check_matches = cursor.fetchall()
            cursor.close()
            connection.close()

            if check_matches:
                logging.info('log in successfully')
                request.session['user'] = email
                logging.info('session ID: ' + request.session['user'])
                return HttpResponseRedirect(reverse('App:customer_index'))
            else:
                return render(request, 'customer/login.html',
                              {'form': form, 'message': 'Wrong password/email Please try again!',
                               'need_to_signup': False})
    else:
        form = CustomerLoginForm()
        print('no response!')
    return render(request, 'customer/login.html', {'form': form})


def login_staff(request):
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            check_username = Staff.objects.filter(username__exact=username)  # check if email exists
            hashed_password = hashed(password)
            if not check_username:
                return render(request, 'staff/login.html',
                              {'form': form, 'message': "username doesn't exist!", 'need_to_signup': True})

            check_matches = Staff.objects.filter(username__exact=username,
                                                 password=hashed_password)  # check if email and password matches
            if check_matches:
                print('log in successfully')
                request.session['user'] = username
                print('session ID: ', request.session['user'])
                return HttpResponseRedirect(reverse('App:staff_index'))
            else:
                return render(request, 'staff/login.html',
                              {'form': form, 'message': 'Wrong password/username Please try again!',
                               'need_to_signup': False})
    else:
        form = StaffLoginForm()
    return render(request, 'staff/login.html', {'form': form})


def login_booking_agent(request):
    if request.method == 'POST':
        form = BookingAgentLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            check_email = BookingAgent.objects.filter(agent_email__exact=email)  # check if email exists
            hashed_password = hashed(password)
            if not check_email:
                return render(request, 'booking_agent/login.html',
                              {'form': form, 'message': "Email address doesn't exist!", 'need_to_signup': True})

            check_matches = BookingAgent.objects.filter(agent_email__exact=email,
                                                        agent_password=hashed_password)  # check if email and password matches
            if check_matches:
                print('log in successfully')
                request.session['user'] = email
                print('session ID: ', request.session['user'])
                return HttpResponseRedirect(reverse('App:agent_index'))
            else:
                return render(request, 'booking_agent/login.html',
                              {'form': form, 'message': 'Wrong password/email Please try again!',
                               'need_to_signup': False})
    else:
        form = BookingAgentLoginForm()
    return render(request, 'booking_agent/login.html', {'form': form})


# Customer use cases
def customer_index(request):
    cursor = connection.cursor()

    email = request.session['user']  # get email (pk) from session

    cursor.execute(f"select name from customer where email = '{email}'")
    customer_name = cursor.fetchall()[0][0]
    print(customer_name)

    sql_str = "select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,A.city as Arrival_city,arrive_airport_name,D.city as Depart_city,depart_airport_name, ticket.sold_price " + \
              "from customer, customer_purchase natural join ticket natural join flight,airport as A, airport as D " + \
              f"where customer.email = customer_purchase.customer_email and email = '{email}' and flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name"
    cursor.execute(sql_str)
    flights = cursor.fetchall()
    cursor.close()
    connection.close()

    if len(flights) > 1:
        history_flights = [flight for flight in flights
                           if previous_than_today(flight[2], flight[3])]
        future_flights = [flight for flight in flights
                          if not previous_than_today(flight[2], flight[3])]
        print(history_flights)
        print(future_flights)
        return render(request, 'customer/index.html',
                      {'customer': customer_name, 'history_flights': history_flights, 'future_flights': future_flights})
    else:
        return render(request, 'customer/index.html',
                      {'customer': customer_name, 'message': "You didn't purchase any ticket!"})


def customer_search(request):
    if request.method == 'POST':
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            SourceCity = form.cleaned_data['SourceCity']
            DepartAirport = form.cleaned_data['DepartAirport']
            DestinationCity = form.cleaned_data['DestinationCity']
            ArriveAirport = form.cleaned_data['ArriveAirport']
            Depart_date = form.cleaned_data['Depart_date']
            Return_date = form.cleaned_data['Return_date']

            # one way trip
            if not Return_date:
                sql_str = "select flight_num,airline_name,depart_date,depart_time,arrival_date,arrival_time,base_price " + \
                          "from flight,airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                          f" and flight.depart_airport_name = '{DepartAirport}' and D.city = '{SourceCity}' and " \
                          f"flight.arrive_airport_name = '{ArriveAirport}' and A.city = '{DestinationCity}' and depart_date = '{Depart_date}'"
                cursor = connection.cursor()
                cursor.execute(sql_str)
                flights = cursor.fetchall()
                cursor.close()
                connection.close()
                if flights:
                    print('one way flight search is successful')
                    return render(request, 'customer/search.html', {'form': form,
                                                                    'flights': flights,
                                                                    'trip_count': 1})
                else:
                    print('cannot find flights')
                    return render(request, 'customer/search.html', {'form': form,
                                                                    'message': 'No flights available!'})

            # round trip
            else:
                sql_str1 = "select flight_num,airline_name,depart_date,depart_time,arrival_date,arrival_time,base_price " + \
                           "from flight,airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                           f" and flight.depart_airport_name = '{DepartAirport}' and D.city = '{SourceCity}' and " \
                           f"flight.arrive_airport_name = '{ArriveAirport}' and A.city = '{DestinationCity}' and depart_date = '{Depart_date}'"

                sql_str2 = "select flight_num,airline_name,depart_date,depart_time,arrival_date,arrival_time,base_price " + \
                           "from flight,airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                           f" and flight.depart_airport_name = '{ArriveAirport}' and D.city = '{DestinationCity}' and " \
                           f"flight.arrive_airport_name = '{DepartAirport}' and A.city = '{SourceCity}' and depart_date = '{Return_date}'"

                cursor = connection.cursor()

                cursor.execute(sql_str1)
                flight_first = cursor.fetchall()

                cursor.execute(sql_str2)
                flight_second = cursor.fetchall()

                cursor.close()
                connection.close()

                if flight_first and flight_second:
                    print("round trip flight search is successful")
                    return render(request, 'customer/search.html', {'form': form,
                                                                    'sourceCity': SourceCity,
                                                                    'destinationCity': DestinationCity,
                                                                    'flight_first': flight_first,
                                                                    'flight_second': flight_second,
                                                                    'trip_count': 2})
                else:
                    print('cannot find flights')
                    return render(request, 'customer/search.html', {'form': form,
                                                                    'message': 'No flights available!'})
    else:
        form = FlightSearchForm(request.POST)
    return render(request, 'customer/search.html', {'form': form})


def customer_purchase(request):
    if request.method == 'POST':
        form = CustomerPurchaseForm(request.POST)
        if form.is_valid():
            flight_num = request.POST.get['flight_num']
            customer_email = form.cleaned_data['email']
            card_type = form.cleaned_data['card_type']
            card_num = form.cleaned_data['card_num']
            name_on_card = form.cleaned_data['name_on_card']
            expire_at = form.cleaned_data['expire_at']
            purchase_date = dt.date.today()
            purchase_time = dt.datetime.now().time()
            t_id = generate_ticket_id(flight_num)
            print('generated_t_id: ', t_id)

            cursor = connection.cursor()
            sql_str1 = f"Insert into customer_purchase(customer_email,ticket_id,card_type,card_num,name_on_card,expire_at,purchase_date,purchase_time)\
                       VALUES ('{customer_email}','{t_id}','{card_type}','{card_num}','{name_on_card}','{expire_at}','{purchase_date}','{purchase_time}')"
            cursor.execute(sql_str1)

            sql_str2 = f"select seats,capacity,ID from ticket natural join flight, airplane \
                        where flight.airplane_id = airplane.ID and ticket.ticket_id = '{t_id}'"
            cursor.execute(sql_str2)
            seats, capacity, ID = cursor.fetchall()[0]
            print('seats: ', seats, 'capacity: ', capacity)

            # check seats
            if seats > 0:
                if seats <= capacity * 0.3:
                    # 70% of tickets have been booked, 20 % increase in ticket price
                    print("Sorry we need to increase the ticket price")
                    cursor.execute(
                        f"update ticket t set t.sold_price = t.sold_price * 1.2 where t.ticket_id = '{t_id}'")
                # update seats
                cursor.execute(f"update airplane a set a.seats = a.seats - 1 where a.ID = '{ID}'")
                print("Ticket successful purchased!")
                print("Remaining seats are ", seats - 1)
                return HttpResponseRedirect(reverse('App:customer_index'))
            else:
                warning_msg = "Sorry, the airplane has reached its capacity!"
                return render(request, 'customer/purchase.html', locals())
    else:
        form = CustomerPurchaseForm()
    return render(request, 'customer/purchase.html', locals())


def customer_comment(request):
    if request.method == 'POST':
        airline_name = request.POST.get('airline_name')
        flight_num = request.POST.get('flight_num')
        depart_date = request.POST.get('depart_date')
        depart_time = request.POST.get('depart_time')
        rating = int(request.POST.get('rating'))
        comment = request.POST.get('comment')
        customer_email = request.session['user']

        # convert str-time to datetime object
        depart_date = convert_str_to_date(depart_date)
        depart_time = convert_str_to_time(depart_time)

        cursor = connection.cursor()
        sql_str = "Insert into rate(customer_email,airline_name,flight_num,depart_date,depart_time,comment,rating) " + \
                  f"VALUES('{customer_email}','{airline_name}','{flight_num}','{depart_date}','{depart_time}','{comment}','{rating}')"
        cursor.execute(sql_str)

        print(sql_str)
        return HttpResponseRedirect(reverse('App:customer_index'))
    return render(request, 'customer/comment.html')


def logout_customer(request):
    del request.session['user']
    return HttpResponseRedirect(reverse('App:login_customer'))
