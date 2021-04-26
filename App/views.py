from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import *
from django.urls import reverse
from App.utils import *
from django.db import connection
from django.contrib.auth.decorators import login_required
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
)


# main page
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


# login and register
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

            logging.info("Successfully created a customer!")

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
            password = hashed(password)
            sql_str = f"insert into staff(username,password,f_name,l_name,date_of_birth,airline_name) values \
                        ('{username}','{password}','{f_name}','{l_name}','{date_of_birth}','{airline_name}')"
            print(sql_str)
            cursor = connection.cursor()
            cursor.execute(sql_str)
            cursor.close()
            connection.close()
            logging.info("Successfully created a staff!")
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
            password = hashed(password)

            cursor = connection.cursor()
            cursor.execute(f"select email from customer where email = '{email}'")

            check_email = cursor.fetchall()
            if not check_email:
                return render(request, 'customer/login.html',
                              {'form': form, 'message': "Email address doesn't exist!", 'need_to_signup': True})

            cursor.execute(f"select email from customer where email = '{email}' and password = '{password}' ")
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
    return render(request, 'customer/login.html', {'form': form})


def login_staff(request):
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            cursor = connection.cursor()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password = hashed(password)

            cursor.execute(f"select * from staff where username = '{username}'")
            check_username = cursor.fetchall()
            if not check_username:
                return render(request, 'staff/login.html',
                              {'form': form, 'message': "username doesn't exist!", 'need_to_signup': True})

            cursor.execute(f"select airline_name from staff where username = '{username}' and password = '{password}'")
            check_matches = cursor.fetchall()
            cursor.close()
            connection.close()
            if check_matches:
                print('log in successfully')
                request.session['user'] = username
                request.session['airline_name'] = check_matches[0][0]
                print('session ID: ', request.session['user'])
                print('session airline_name: ', request.session['airline_name'])
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
    try:
        request.session['user']
    except KeyError:
        return HttpResponseRedirect(reverse('App:login_customer'))

    cursor = connection.cursor()

    email = request.session['user']  # get email (pk) from session

    cursor.execute(f"select name from customer where email = '{email}'")
    customer_name = cursor.fetchall()[0][0]

    sql_str = "select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,A.city as Arrival_city,arrive_airport_name,D.city as Depart_city,depart_airport_name, ticket.sold_price " + \
              "from customer, customer_purchase natural join ticket natural join flight,airport as A, airport as D " + \
              f"where customer.email = customer_purchase.customer_email and email = '{email}' and flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name"
    cursor.execute(sql_str)
    flights = cursor.fetchall()
    cursor.close()
    connection.close()

    print(flights)

    if len(flights) > 0 and len(flights[0]) > 0:
        # history flights: arrive_datetime < now
        # future flights: depart_datetime > now
        history_flights = [flight for flight in flights
                           if previous_than_today(flight[4], flight[5])]
        future_flights = [flight for flight in flights
                          if later_than_today(flight[2], flight[3])]
        current_flight = [flight for flight in flights if
                          flight not in history_flights and flight not in future_flights]
        print(history_flights)
        print(future_flights)
        print(current_flight)
        return render(request, 'customer/index.html',
                      {'customer': customer_name, 'history_flights': history_flights, 'future_flights': future_flights,
                       'current_flights': current_flight})
    else:
        return render(request, 'customer/index.html',
                      {'customer': customer_name, 'message': "You didn't purchase any ticket!"})


def customer_search(request):
    try:
        request.session['user']
    except KeyError:
        return HttpResponseRedirect(reverse('App:login_customer'))

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
    try:
        request.session['user']
    except KeyError:
        return HttpResponseRedirect(reverse('App:login_customer'))
    if request.method == 'POST':
        form = CustomerPurchaseForm(request.POST)
        if form.is_valid():
            flight_num = request.POST.get('flight_num')
            logging.info(flight_num)
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
                cursor.close()
                connection.close()
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
    try:
        request.session['user']
    except KeyError:
        return HttpResponseRedirect(reverse('App:login_customer'))
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
        cursor.close()
        connection.close()
        return HttpResponseRedirect(reverse('App:customer_index'))
    return render(request, 'customer/comment.html')


def logout_customer(request):
    try:
        request.session['user']
    except KeyError:
        return HttpResponseRedirect(reverse('App:login_customer'))
    del request.session['user']
    return HttpResponseRedirect(reverse('App:login_customer'))


def customer_spending(request):
    try:
        request.session['user']
    except KeyError:
        return HttpResponseRedirect(reverse('App:login_customer'))

    customer_email = request.session['user']
    if request.method == 'GET':
        logging.info(customer_email)
        cursor = connection.cursor()
        sql_str1 = f"select SUM(sold_price) from customer_purchase natural join ticket \
                    where customer_email = '{customer_email}' and YEAR(purchase_date) = YEAR(CURDATE()) - 1"
        cursor.execute(sql_str1)
        data1 = cursor.fetchall()[0][0]
        # last 6 months
        sql_str2 = f"select MONTH(purchase_date), sold_price from customer_purchase natural join ticket \
                    where customer_email = '{customer_email}' and (((MONTH(CURDATE()) - MONTH(purchase_date)) between 1 and 6) or (MONTH(CURDATE()) - MONTH(purchase_date)) <= -6) \
                    group by MONTH(purchase_date),sold_price;"
        logging.info(sql_str2)
        cursor.execute(sql_str2)
        res = cursor.fetchall()
        logging.info(res)
        data2 = [[convert_to_month(r[0]), r[1]] for r in res]
        cursor.close()
        connection.close()
        logging.info(data2)
        return render(request, 'customer/spending.html', {'data1': data1, 'data2': data2, 'monthDiff': 6})

    elif request.method == 'POST':
        cursor = connection.cursor()
        startYear = int(request.POST.get('startYear'))
        startMonth = int(request.POST.get('startMonth'))
        endYear = int(request.POST.get('endYear'))
        endMonth = int(request.POST.get('endMonth'))

        if startYear == endYear:
            monthDiff = endMonth - startMonth + 1
            sql_str1 = f"select SUM(sold_price) from customer_purchase natural join ticket \
                                    where customer_email = '{customer_email}' and ({endMonth + 1} - MONTH(purchase_date)) between 1 and {monthDiff} and YEAR(purchase_date) = {startYear}"

            sql_str2 = f"select MONTH(purchase_date), sold_price from customer_purchase natural join ticket \
                                    where customer_email = '{customer_email}' and ({endMonth + 1} - MONTH(purchase_date)) between 1 and {monthDiff} and YEAR(purchase_date) = {startYear} \
                                    group by MONTH(purchase_date), sold_price;"
        else:
            monthDiff = (endMonth + 12 * (endYear - startYear)) - startMonth + 1
            temp_diff = endMonth + 1 - startMonth

            sql_str1 = f"select SUM(sold_price) from customer_purchase natural join ticket \
                        where customer_email = '{customer_email}' and (({endMonth + 1} - MONTH(purchase_date)) between 1 and {monthDiff} or ({endMonth + 1} - MONTH(purchase_date)) <= {temp_diff})"

            sql_str2 = f"select MONTH(purchase_date), sold_price from customer_purchase natural join ticket \
                        where customer_email = '{customer_email}' and (({endMonth + 1} - MONTH(purchase_date)) between 1 and {monthDiff} or ({endMonth + 1} - MONTH(purchase_date)) <= {temp_diff}) \
                        group by MONTH(purchase_date), sold_price;"

        cursor.execute(sql_str1)
        data1 = cursor.fetchall()[0][0]
        cursor.execute(sql_str2)
        res = cursor.fetchall()
        data2 = [[convert_to_month(r[0]), r[1]] for r in res]
        cursor.close()
        connection.close()
        logging.info(data2)

        return render(request, 'customer/spending.html', {'data1': data1, 'data2': data2, 'monthDiff': monthDiff})


# Staff use cases
def staff_index(request):
    try:
        username = request.session['user']
    except KeyError:
        return HttpResponseRedirect(reverse('App:login_staff'))
    cursor = connection.cursor()
    cursor.execute(f"select * from staff where username = '{username}'")
    staff = cursor.fetchall()[0]
    airline_name = staff[-1]

    if request.method == 'GET':
        cursor.execute(
            f"select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,status,A.city as Arrival_city,arrive_airport_name as arrive_airport,D.city as Depart_city,depart_airport_name as depart_airport "
            f" from flight,airport as D,airport as A where airline_name = '{airline_name}' and flight.arrive_airport_name = A.name "
            f"and flight.depart_airport_name = D.name")
        flights = cursor.fetchall()
        print(flights)
        cursor.close()
        connection.close()

        if len(flights) > 0 and len(flights[0]) > 0:
            # future flights: depart_datetime > now
            # history flights: arrive_datetime < now
            # current_flights: depart_datetime < now and arrive_datetime > now
            future_flights = [f for f in flights if later_than_today(f[2], f[3]) and before_next_days(f[2], f[3], 30)]

            # dates, airports, cities
            # history_flights = [f for f in flights if previous_than_today(f[4], f[5])]
            # current_flights = [f for f in flights if
            #                    previous_than_today(f[2], f[3]) and later_than_today(f[4], f[5])]
            logging.info(future_flights)
            # logging.info(history_flights)
            # logging.info(current_flights)

            return render(request, 'staff/index.html',
                          {'staff': staff, 'future_flights': future_flights})
        else:
            return render(request, 'staff/index.html',
                          {'staff': staff, 'message': "No future flights!"})

    if request.method == 'POST':
        startDate = convert_str_to_date_YYYYMMDD(request.POST.get('startDate'))
        endDate = convert_str_to_date_YYYYMMDD(request.POST.get('endDate'))
        sourceCity = request.POST.get('sourceCity')
        arriveCity = request.POST.get('arriveCity')
        sourceAirport = request.POST.get('sourceAirport')
        arriveAirport = request.POST.get('arriveAirport')

        sql_str = f"select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,status,A.city as Arrival_city,arrive_airport_name as arrive_airport,D.city as Depart_city,depart_airport_name as depart_airport \
                from flight,airport as D,airport as A where airline_name = '{airline_name}' and flight.arrive_airport_name = A.name \
             and flight.depart_airport_name = D.name and D.city = '{sourceCity}' and depart_airport_name = '{sourceAirport}' and A.city = '{arriveCity}' and arrive_airport_name = '{arriveAirport}' \
             and depart_date between '{startDate}' and '{endDate}'"
        cursor.execute(sql_str)

        flights = cursor.fetchall()
        cursor.close()
        connection.close()
        print('search results:', flights, 'len = ', len(flights))

        if len(flights) > 0 and len(flights[0]) > 0:
            # future flights: depart_datetime > now
            # history flights: arrive_datetime < now
            # current_flights: depart_datetime < now and arrive_datetime > now
            future_flights = [f for f in flights if later_than_today(f[2], f[3])]

            # dates, airports, cities
            history_flights = [f for f in flights if previous_than_today(f[4], f[5])]
            current_flights = [f for f in flights if
                               previous_than_today(f[2], f[3]) and later_than_today(f[4], f[5])]
            logging.info(future_flights)
            logging.info(history_flights)
            logging.info(current_flights)

            return render(request, 'staff/index.html',
                          {'staff': staff, 'future_flights': future_flights, 'history_flights': history_flights,
                           'current_flights': current_flights})

        else:
            return render(request, 'staff/index.html',
                          {'staff': staff, 'message': "No available flights based on search results!"})


def view_customers_staff(request):
    try:
        request.session['user']
    except KeyError:
        return HttpResponseRedirect(reverse('App:login_staff'))

    if request.method == 'GET':
        return render(request, 'staff/view_customers.html', {})
    elif request.method == 'POST':
        flight_num = request.POST.get('flight_num')
        cursor = connection.cursor()
        # customer-purchase
        sql_str1 = "select c.name from flight natural join ticket natural join customer_purchase as cp,customer as c where " \
                   f"cp.customer_email = c.email and flight.flight_num = '{flight_num}'"
        # agent_purchase
        sql_str2 = "select c.name from flight natural join ticket natural join agent_purchase as ap, customer as c where " \
                   f"ap.customer_email = c.email and flight.flight_num = '{flight_num}'"

        cursor.execute(sql_str1)
        customer_names = cursor.fetchall()
        cursor.execute(sql_str2)
        agent_customer_names = cursor.fetchall()

        if agent_customer_names:
            customer_names += agent_customer_names
        logging.info(customer_names)

        if len(customer_names) > 0 and len(customer_names[0]) > 0:
            return render(request, 'staff/view_customers.html',
                          {'customer_names': customer_names, 'flight_num': flight_num})
        else:
            return render(request, 'staff/view_customers.html', {'message': 'No customers in this flight!'})


def create_flight_staff(request):
    try:
        username, airline_name = request.session['user'], request.session['airline_name']
    except KeyError:
        return HttpResponseRedirect(reverse('App:login_staff'))

    if request.method == 'GET':
        cursor = connection.cursor()
        cursor.execute(f"select distinct airplane_id from flight where airline_name = '{airline_name}'")
        airplane_ids = cursor.fetchall()

        cursor.execute("select name from airport")
        airports = cursor.fetchall()
        cursor.close()
        connection.close()
        return render(request, 'staff/create_flight.html', {'airplane_ids': airplane_ids, 'airports': airports})
    elif request.method == 'POST':
        flight_num = request.POST.get('flight_num')
        depart_date = request.POST.get('depart_date')
        depart_time = request.POST.get('depart_time')
        arrive_date = request.POST.get('arrive_date')
        arrive_time = request.POST.get('arrive_time')
        airplane_id = request.POST.get('airplane_id')
        base_price = request.POST.get('base_price')
        status = request.POST.get('status')
        arrive_airport_name = request.POST.get('arrive_airport_name')
        depart_airport_name = request.POST.get('depart_airport_name')

        cursor = connection.cursor()
        sql_str = "Insert into flight(airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,airplane_id,base_price,status,arrive_airport_name,depart_airport_name)" \
                  f"VALUES ('{airline_name}','{flight_num}','{depart_date}','{depart_time}','{arrive_date}','{arrive_time}','{airplane_id}','{base_price}','{status}','{arrive_airport_name}','{depart_airport_name}')"
        cursor.execute(sql_str)
        return HttpResponseRedirect(reverse('App:staff_index'))


def change_flight_status(request):
    try:
        request.session['user']
    except KeyError:
        return HttpResponseRedirect(reverse('App:login_staff'))

    if request.method == 'GET':
        return render(request, 'staff/change_status.html')
    elif request.method == 'POST':
        newStatus = request.POST.get('newStatus')
        airline_name = request.POST.get('airline_name')
        flight_num = request.POST.get('flight_num')
        depart_date = request.POST.get('depart_date')
        depart_time = request.POST.get('depart_time')

        depart_date = convert_str_to_date(depart_date)
        depart_time = convert_str_to_time(depart_time)

        cursor = connection.cursor()
        sql_str = f"UPDATE flight SET status = '{newStatus}' WHERE airline_name = '{airline_name}' and flight_num = '{flight_num}' and depart_date = '{depart_date}' and depart_time = '{depart_time}'"
        cursor.execute(sql_str)
        cursor.close()
        connection.close()
        return HttpResponseRedirect(reverse('App:staff_index'))


def add_airplane_staff(request):
    try:
        airline_name = request.session['airline_name']
    except KeyError:
        return HttpResponseRedirect(reverse('App:login_staff'))

    cursor = connection.cursor()

    if request.method == 'POST':
        airplane_id = request.POST.get('airplane_id')
        seats = int(request.POST.get('seats'))

        cursor.execute(
            f"INSERT INTO airplane(ID,airline_name,seats,capacity) VALUES('{airplane_id}','{airline_name}',{seats},{seats})")

    cursor.execute(f"select ID,capacity from airplane where airline_name = '{airline_name}'")
    airplane_info = cursor.fetchall()
    cursor.close()
    connection.close()
    return render(request, 'staff/add_airplane.html', {'airplane_info': airplane_info, 'airline_name': airline_name})


def add_airport_staff(request):
    try:
        airline_name = request.session['airline_name']
    except KeyError:
        return HttpResponseRedirect(reverse('App:login_staff'))

    cursor = connection.cursor()
    if request.method == 'POST':
        airport_name = request.POST.get('airport_name')
        airport_city = request.POST.get('airport_city')

        cursor.execute(f"INSERT INTO airport(name,city) VALUES('{airport_name}','{airport_city}')")

    cursor.execute("select * from airport order by city ASC")
    airports = cursor.fetchall()
    cursor.close()
    connection.close()
    return render(request, 'staff/add_airport.html', {'airports': airports})


def view_flight_ratings(request):
    try:
        request.session['user']
    except KeyError:
        return HttpResponseRedirect(reverse('App:login_staff'))

    if request.method == 'POST':
        cursor = connection.cursor()
        airline_name = request.POST.get('airline_name')
        flight_num = request.POST.get('flight_num')
        depart_date = request.POST.get('depart_date')
        depart_time = request.POST.get('depart_time')

        depart_date = convert_str_to_date(depart_date)
        depart_time = convert_str_to_time(depart_time)

        sql_str1 = f"select AVG(rating) from rate natural join flight where airline_name = '{airline_name}' and flight_num = '{flight_num}' and depart_date = '{depart_date}' and depart_time = '{depart_time}'"
        sql_str2 = f"select comment,rating from rate natural join flight where airline_name = '{airline_name}' and flight_num = '{flight_num}' and depart_date = '{depart_date}' and depart_time = '{depart_time}'"

        cursor.execute(sql_str1)
        avg_rating = cursor.fetchall()

        null_msg = False

        if not avg_rating[0][0]:
            null_msg = True
        else:
            avg_rating = round(avg_rating[0][0],2)

        cursor.execute(sql_str2)
        infos = cursor.fetchall()

        cursor.close()
        connection.close()
        return render(request, 'staff/view_flight_ratings.html',
                      {'avg_rating': avg_rating, 'infos': infos, 'form': False, 'null_msg': null_msg})

    return render(request, 'staff/view_flight_ratings.html', {'form': True})


def logout_staff(request):
    try:
        request.session['user']
    except KeyError:
        return HttpResponseRedirect(reverse('App:login_staff'))

    del request.session['user']
    return HttpResponseRedirect(reverse('App:login_staff'))
