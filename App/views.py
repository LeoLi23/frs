from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from App.utils import *
from django.db import connection
import logging
from dateutil.relativedelta import relativedelta

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
                args = (DepartAirport, SourceCity, ArriveAirport, DestinationCity, Depart_date)
                sql_str = "select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time " + \
                          "from flight,airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                          f" and flight.depart_airport_name = %s and D.city = %s and " \
                          f"flight.arrive_airport_name = %s and A.city = %s and depart_date = %s;"
                cursor = connection.cursor()
                cursor.execute(sql_str, args)
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
                args1 = (DepartAirport, SourceCity, ArriveAirport, DestinationCity, Depart_date)
                sql_str1 = "select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time " + \
                           "from flight,airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                           f" and flight.depart_airport_name = %s and D.city = %s and " \
                           f"flight.arrive_airport_name = %s and A.city = %s and depart_date = %s"

                args2 = (ArriveAirport, DestinationCity, DepartAirport, SourceCity, Return_date)
                sql_str2 = "select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time " + \
                           "from flight,airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                           f" and flight.depart_airport_name = %s and D.city = %s and " \
                           f"flight.arrive_airport_name = %s and A.city = %s and depart_date = %s"

                cursor = connection.cursor()

                cursor.execute(sql_str1, args1)
                flight_first = cursor.fetchall()

                cursor.execute(sql_str2, args2)
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

            password = hashed(password)

            args = (email, name, password, building_num, street, city, state, phone_num, passport_num, passport_country,
                    passport_expire, date_of_birth)
            sql_str = "Insert into customer(email,name,password,building_num,street,city,state,phone_num,passport_num,passport_country,passport_expire,date_of_birth) " + \
                      "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

            cursor = connection.cursor()
            cursor.execute(sql_str, args)
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

            args = (username, password, f_name, l_name, date_of_birth, airline_name)

            sql_str = "Insert into staff(username,password,f_name,l_name,date_of_birth,airline_name) values \
                        (%s, %s, %s, %s, %s, %s);"

            cursor = connection.cursor()
            cursor.execute(sql_str, args)
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

            cursor = connection.cursor()
            args = (agent_email, agent_id, hashed_password)
            sql_str = "Insert into booking_agent(agent_email, agent_id, agent_password) VALUES(%s, %s, %s);"
            cursor.execute(sql_str, args)

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
            cursor.execute("select email from customer where email = %s;", email)

            check_email = cursor.fetchall()
            if not check_email:
                return render(request, 'customer/login.html',
                              {'form': form, 'message': "Email address doesn't exist!", 'need_to_signup': True})

            cursor.execute("select email from customer where email = %s and password = %s;", (email, password))
            check_matches = cursor.fetchall()
            cursor.close()
            connection.close()
            if check_matches:
                logging.info('log in successfully')
                request.session['user'] = email
                request.session['user_type'] = 'customer'
                logging.info('session ID: ' + request.session['user'])
                return HttpResponseRedirect(reverse('App:customer_index'))
            else:
                print('invalid password')
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

            cursor.execute(f"select * from staff where username = %s;", username)
            check_username = cursor.fetchall()
            if not check_username:
                return render(request, 'staff/login.html',
                              {'form': form, 'message': "username doesn't exist!", 'need_to_signup': True})

            cursor.execute(f"select airline_name from staff where username = %s and password = %s;",
                           (username, password))
            check_matches = cursor.fetchall()
            cursor.close()
            connection.close()
            if check_matches:
                print('log in successfully')
                request.session['user'] = username
                request.session['airline_name'] = check_matches[0][0]
                request.session['user_type'] = 'staff'
                print('session ID: ', request.session['user'])
                print('session airline_name: ', request.session['airline_name'])
                print('user type: ', request.session['user_type'])
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
            agent_id = form.cleaned_data['agent_id']
            password = form.cleaned_data['password']
            hashed_password = hashed(password)

            # check if email exists
            cursor = connection.cursor()
            cursor.execute("select * from booking_agent where agent_email = %s;", email)
            check_email = cursor.fetchall()

            if not check_email:
                return render(request, 'booking_agent/login.html',
                              {'form': form, 'message': "Email address doesn't exist!", 'need_to_signup': True})

            cursor.execute("select * from booking_agent where agent_email = %s and agent_password = %s;",
                           (email, hashed_password))
            check_matches = cursor.fetchall()
            cursor.close()
            connection.close()

            if check_matches:
                print('log in successfully')
                request.session['user'] = email
                request.session['user_type'] = 'agent'
                request.session['agent_id'] = agent_id
                print('session ID: ', request.session['user'])
                print('agent ID: ', request.session['agent_id'])
                return HttpResponseRedirect(reverse('App:agent_index'))
            else:
                return render(request, 'booking_agent/login.html',
                              {'form': form, 'message': 'Wrong password/email Please try again!',
                               'need_to_signup': False})
    else:
        form = BookingAgentLoginForm()
    return render(request, 'booking_agent/login.html', {'form': form})


# Customer use cases
@login_check_customer
def customer_index(request):
    cursor = connection.cursor()

    email = request.session['user']  # get email (pk) from session

    cursor.execute("select name from customer where email = %s;", email)
    customer_name = cursor.fetchall()[0][0]

    sql_str = "SELECT airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,A.city as Arrival_city,arrive_airport_name,D.city as Depart_city,depart_airport_name, ticket.sold_price " + \
              "from customer, customer_purchase natural join ticket natural join flight,airport as A, airport as D " + \
              "where customer.email = customer_purchase.customer_email and email = %s and flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name"
    cursor.execute(sql_str, email)
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


@login_check_customer
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
                args = (DepartAirport, SourceCity, ArriveAirport, DestinationCity, Depart_date)
                sql_str = "select flight_num,airline_name,depart_date,depart_time,arrival_date,arrival_time,base_price " + \
                          "from flight,airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                          f" and flight.depart_airport_name = %s and D.city = %s and " \
                          f"flight.arrive_airport_name = %s and A.city = %s and depart_date = %s;"
                cursor = connection.cursor()
                cursor.execute(sql_str, args)
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
                args1 = (DepartAirport, SourceCity, ArriveAirport, DestinationCity, Depart_date)
                args2 = (ArriveAirport, DestinationCity, DepartAirport, SourceCity, Return_date)
                sql_str1 = "select flight_num,airline_name,depart_date,depart_time,arrival_date,arrival_time,base_price " + \
                           "from flight,airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                           f" and flight.depart_airport_name = %s and D.city = %s and " \
                           f"flight.arrive_airport_name = %s and A.city = %s and depart_date = %s;"

                sql_str2 = "select flight_num,airline_name,depart_date,depart_time,arrival_date,arrival_time,base_price " + \
                           "from flight,airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                           f" and flight.depart_airport_name = %s and D.city = %s and " \
                           f"flight.arrive_airport_name = %s and A.city = %s and depart_date = %s;"

                cursor = connection.cursor()

                cursor.execute(sql_str1, args1)
                flight_first = cursor.fetchall()

                cursor.execute(sql_str2, args2)
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


@login_check_customer
def customer_purchase(request):
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
            args = (customer_email, t_id, card_type, card_num, name_on_card, expire_at, purchase_date, purchase_time)
            sql_str1 = "Insert into customer_purchase(customer_email,ticket_id,card_type,card_num,name_on_card,expire_at,purchase_date,purchase_time) \
                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(sql_str1, args)

            sql_str2 = f"select seats,capacity,ID from ticket natural join flight, airplane \
                        where flight.airplane_id = airplane.ID and ticket.ticket_id = %s;"
            cursor.execute(sql_str2, t_id)
            seats, capacity, ID = cursor.fetchall()[0]
            print('seats: ', seats, 'capacity: ', capacity)

            # check seats
            if seats > 0:
                if seats <= capacity * 0.3:
                    # 70% of tickets have been booked, 20 % increase in ticket price
                    print("Sorry we need to increase the ticket price")
                    cursor.execute(
                        "update ticket t set t.sold_price = t.sold_price * 1.2 where t.ticket_id = %s;", t_id)
                # update seats
                cursor.execute("update airplane a set a.seats = a.seats - 1 where a.ID = %s;", ID)
                cursor.close()
                connection.close()
                print("Ticket successfully purchased!")
                print("Remaining seats are ", seats - 1)
                return HttpResponseRedirect(reverse('App:customer_index'))
            else:
                warning_msg = "Sorry, the airplane has reached its capacity!"
                return render(request, 'customer/purchase.html', locals())
    else:
        form = CustomerPurchaseForm()
    return render(request, 'customer/purchase.html', locals())


@login_check_customer
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
        args = (customer_email, airline_name, flight_num, depart_date, depart_time, comment, rating)
        sql_str = "Insert into rate(customer_email,airline_name,flight_num,depart_date,depart_time,comment,rating) " + \
                  "VALUES(%s,%s,%s,%s,%s,%s,%s);"
        cursor.execute(sql_str, args)
        cursor.close()
        connection.close()
        return HttpResponseRedirect(reverse('App:customer_index'))
    return render(request, 'customer/comment.html')


@login_check_customer
def logout_customer(request):
    del request.session['user']
    del request.session['user_type']
    return HttpResponseRedirect(reverse('App:login_customer'))


@login_check_customer
def customer_spending(request):
    customer_email = request.session['user']
    if request.method == 'GET':
        logging.info(customer_email)
        cursor = connection.cursor()
        sql_str1 = f"select SUM(sold_price) from customer_purchase natural join ticket \
                    where customer_email = %s and YEAR(purchase_date) = YEAR(CURDATE()) - 1"

        cursor.execute(sql_str1, customer_email)
        data1 = cursor.fetchall()[0][0]

        today = dt.date.today()
        delta = relativedelta(months=6)
        six_months_prev = today - delta
        # last 6 months
        sql_str2 = f"select MONTH(purchase_date), SUM(sold_price) from customer_purchase natural join ticket \
                    where customer_email = %s and (purchase_date between %s and %s) \
                    group by MONTH(purchase_date);"

        cursor.execute(sql_str2, (customer_email, six_months_prev, today))
        res = cursor.fetchall()

        data2 = [[convert_to_month(r[0]), r[1]] for r in res]
        cursor.close()
        connection.close()

        logging.info(data2)

        print('six_months_prev: ', six_months_prev)

        return render(request, 'customer/spending.html',
                      {'data1': data1, 'data2': data2, 'default': True, 'startDate': six_months_prev, 'endDate': today})

    elif request.method == 'POST':
        cursor = connection.cursor()
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')

        args = (customer_email, startDate, endDate)
        sql_str1 = "select SUM(sold_price) from customer_purchase natural join ticket where customer_email = %s and " \
                   "(purchase_date between %s and %s);"
        sql_str2 = "select MONTH(purchase_date), SUM(sold_price) from customer_purchase natural join ticket \
                    where customer_email = %s and (purchase_date between %s and %s) \
                    group by MONTH(purchase_date);"

        cursor.execute(sql_str1, args)
        data1 = cursor.fetchall()[0][0]

        cursor.execute(sql_str2, args)
        res = cursor.fetchall()
        data2 = [[convert_to_month(r[0]), r[1]] for r in res]
        cursor.close()
        connection.close()
        logging.info(data2)

        return render(request, 'customer/spending.html',
                      {'data1': data1, 'data2': data2, 'startDate': startDate, 'endDate': endDate, 'default': False})


# Staff use cases
@login_check_staff
def staff_index(request):
    cursor = connection.cursor()
    username = request.session['user']
    airline_name = request.session['airline_name']
    cursor.execute("select * from staff where username = %s;", username)
    staff = cursor.fetchall()[0]

    if request.method == 'GET':
        cursor.execute(
            "select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,status,A.city as Arrival_city,arrive_airport_name as arrive_airport,D.city as Depart_city,depart_airport_name as depart_airport "
            " from flight,airport as D,airport as A where airline_name = %s and flight.arrive_airport_name = A.name "
            "and flight.depart_airport_name = D.name", airline_name)
        flights = cursor.fetchall()
        print(flights)
        cursor.close()
        connection.close()

        if len(flights) > 0 and len(flights[0]) > 0:
            # future flights: depart_datetime > now
            # history flights: arrive_datetime < now
            # current_flights: depart_datetime < now and arrive_datetime > now
            future_flights = [f for f in flights if later_than_today(f[2], f[3]) and before_next_days(f[2], f[3], 30)]
            logging.info(future_flights)
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

        args = (airline_name, sourceCity, sourceAirport, arriveCity, arriveAirport, startDate, endDate)

        sql_str = f"select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,status,A.city as Arrival_city,arrive_airport_name as arrive_airport,D.city as Depart_city,depart_airport_name as depart_airport \
                from flight,airport as D,airport as A where airline_name = %s and flight.arrive_airport_name = A.name \
             and flight.depart_airport_name = D.name and D.city = %s and depart_airport_name = %s and A.city = %s and arrive_airport_name = %s \
             and depart_date between %s and %s;"

        cursor.execute(sql_str, args)

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


@login_check_staff
def view_customers_staff(request):
    if request.method == 'GET':
        return render(request, 'staff/view_customers.html', {})
    elif request.method == 'POST':
        flight_num = request.POST.get('flight_num')
        cursor = connection.cursor()
        # customer-purchase
        sql_str1 = "select c.name from flight natural join ticket natural join customer_purchase as cp,customer as c where " \
                   f"cp.customer_email = c.email and flight.flight_num = %s"
        # agent_purchase
        sql_str2 = "select c.name from flight natural join ticket natural join agent_purchase as ap, customer as c where " \
                   f"ap.customer_email = c.email and flight.flight_num = %s"

        cursor.execute(sql_str1, flight_num)
        customer_names = cursor.fetchall()
        cursor.execute(sql_str2, flight_num)
        agent_customer_names = cursor.fetchall()

        print('customers:', customer_names)
        print('agent customers: ', agent_customer_names)

        if agent_customer_names and customer_names:
            customer_names += agent_customer_names
        elif not customer_names:  # if customer names are None, replace it with agent purchase names
            customer_names = agent_customer_names

        logging.info(customer_names)

        if len(customer_names) > 0 and len(customer_names[0]) > 0:
            return render(request, 'staff/view_customers.html',
                          {'customer_names': customer_names, 'flight_num': flight_num})
        else:
            return render(request, 'staff/view_customers.html', {'message': 'No customers in this flight!'})


@login_check_staff
def create_flight_staff(request):
    username, airline_name = request.session['user'], request.session['airline_name']
    if request.session['user_type'] != 'staff':
        return HttpResponse("You are not authorized to perform this action!")
    if request.method == 'GET':
        cursor = connection.cursor()
        cursor.execute("select distinct airplane_id from flight where airline_name = %s", airline_name)
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
        args = (
            airline_name, flight_num, depart_date, depart_time, arrive_date, arrive_time, airplane_id, base_price,
            status,
            arrive_airport_name, depart_airport_name)
        sql_str = "Insert into flight(airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,airplane_id,base_price,status,arrive_airport_name,depart_airport_name)" \
                  f"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql_str, args)
        return HttpResponseRedirect(reverse('App:staff_index'))


@login_check_staff
def change_flight_status(request):
    if request.session['user_type'] != 'staff':
        return HttpResponse("You are not authorized to perform this action!")

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
        args = (newStatus, airline_name, flight_num, depart_date, depart_time)
        sql_str = f"UPDATE flight SET status = %s WHERE airline_name = %s and flight_num = %s and depart_date = %s and depart_time = %s;"
        cursor.execute(sql_str, args)
        cursor.close()
        connection.close()
        return HttpResponseRedirect(reverse('App:staff_index'))


@login_check_staff
def add_airplane(request):
    if request.session['user_type'] != 'staff':
        return HttpResponse("You are not authorized to perform this action!")

    airline_name = request.session['airline_name']
    cursor = connection.cursor()

    if request.method == 'POST':
        airplane_id = request.POST.get('airplane_id')
        seats = int(request.POST.get('seats'))
        args = (airplane_id, airline_name, seats, seats)
        cursor.execute(
            "INSERT INTO airplane(ID,airline_name,seats,capacity) VALUES(%s, %s, %s, %s)", args)

    cursor.execute("select ID,capacity from airplane where airline_name = %s", airline_name)
    airplane_info = cursor.fetchall()
    cursor.close()
    connection.close()
    return render(request, 'staff/add_airplane.html', {'airplane_info': airplane_info, 'airline_name': airline_name})


@login_check_staff
def add_airport_staff(request):
    if request.session['user_type'] != 'staff':
        return HttpResponse("You are not authorized to perform this action!")

    cursor = connection.cursor()
    if request.method == 'POST':
        airport_name = request.POST.get('airport_name')
        airport_city = request.POST.get('airport_city')

        cursor.execute("INSERT INTO airport(name,city) VALUES(%s, %s)", (airport_name, airport_city))

    cursor.execute("select * from airport order by city ASC;")
    airports = cursor.fetchall()
    cursor.close()
    connection.close()
    return render(request, 'staff/add_airport.html', {'airports': airports})


@login_check_staff
def view_flight_ratings(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        airline_name = request.POST.get('airline_name')
        flight_num = request.POST.get('flight_num')
        depart_date = request.POST.get('depart_date')
        depart_time = request.POST.get('depart_time')

        depart_date = convert_str_to_date(depart_date)
        depart_time = convert_str_to_time(depart_time)

        args = (airline_name, flight_num, depart_date, depart_time)

        sql_str1 = f"select AVG(rating) from rate natural join flight where airline_name = %s and flight_num = %s and depart_date = %s and depart_time = %s"
        sql_str2 = f"select comment,rating from rate natural join flight where airline_name = %s and flight_num = %s and depart_date = %s and depart_time = %s"

        cursor.execute(sql_str1, args)
        avg_rating = cursor.fetchall()

        null_msg = False

        if not avg_rating[0][0]:
            null_msg = True
        else:
            avg_rating = round(avg_rating[0][0], 2)

        cursor.execute(sql_str2, args)
        infos = cursor.fetchall()

        cursor.close()
        connection.close()
        return render(request, 'staff/view_flight_ratings.html',
                      {'avg_rating': avg_rating, 'infos': infos, 'form': False, 'null_msg': null_msg})

    return render(request, 'staff/view_flight_ratings.html', {'form': True})


@login_check_staff
def view_most_frequent_customers(request):
    airline_name = request.session['airline_name']
    cursor = connection.cursor()
    sql_str = "select customer_email,count(*) from ticket natural join customer_purchase where airline_name=%s and YEAR(purchase_date) = YEAR(CURDATE()) - 1 group by customer_email order by count(*) desc limit 5"
    cursor.execute(sql_str, airline_name)
    customer_infos = cursor.fetchall()
    print("customer_infos: ", customer_infos)
    return render(request, 'staff/most_frequent_customers.html', {'customer_infos': customer_infos})


@login_check_staff
def view_flights_for_one_customer(request):
    if request.method == 'POST':
        customer_email = request.POST.get('customer_email')

        print('choose customer: ', customer_email)

        cursor = connection.cursor()
        args = (request.session['airline_name'], customer_email)
        sql_str = "select flight_num, depart_date, depart_time, depart_airport_name, arrive_airport_name from flight natural join ticket natural join customer_purchase as cp, customer c where cp.customer_email = c.email and airline_name = %s and c.email = %s order by depart_date, depart_time ASC;"
        cursor.execute(sql_str, args)
        flight_infos = cursor.fetchall()

        print(flight_infos)

        return render(request, 'staff/view_flights_for_one_customer.html',
                      {'form': False, 'flight_infos': flight_infos, 'customer_email': customer_email})
    return render(request, 'staff/view_flights_for_one_customer.html', {'form': True})


@login_check_staff
def view_reports_staff(request):
    if request.method == 'POST':
        airline_name = request.session['airline_name']
        cursor = connection.cursor()
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')

        args = (airline_name, startDate, endDate)
        # customer purchase
        sql_str1 = "select SUM(sold_price) from customer_purchase natural join ticket \
                    where airline_name = %s and (purchase_date between %s and %s);"

        sql_str2 = "select MONTH(purchase_date), SUM(sold_price) from customer_purchase natural join ticket \
                               where airline_name = %s and (purchase_date between %s and %s) \
                                group by MONTH(purchase_date) order by MONTH(purchase_date);"

        # agent_purchase
        sql_str3 = "select SUM(sold_price) from agent_purchase natural join ticket \
                    where airline_name = %s and (purchase_date between %s and %s);"

        sql_str4 = "select MONTH(purchase_date), SUM(sold_price) from agent_purchase natural join ticket \
                               where airline_name = %s and (purchase_date between %s and %s) \
                                group by MONTH(purchase_date) order by MONTH(purchase_date);"

        cursor.execute(sql_str1, args)
        data1_a = cursor.fetchall()[0][0]

        cursor.execute(sql_str3, args)
        data1_b = cursor.fetchall()[0][0]

        if data1_b is None:
            data1_b = 0
        if data1_a is None:
            data1_a = 0

        data1 = data1_a + data1_b
        cursor.execute(sql_str2, args)
        res1 = cursor.fetchall()

        cursor.execute(sql_str4, args)
        res2 = cursor.fetchall()

        res = res1 + res2

        data2 = [[convert_to_month(r[0]), r[1]] for r in res]

        print('data1: ', data1)
        print('data2: ', data2)

        cursor.close()
        connection.close()
        default = False
        return render(request, 'staff/view_reports.html', locals())

    if request.method == 'GET':
        return render(request, 'staff/view_reports.html', {'default': True})


@login_check_staff
def view_top_destinations(request):
    airline_name = request.session['airline_name']
    cursor = connection.cursor()

    today = dt.date.today()
    delta = relativedelta(months=3)
    three_months_prev = today - delta

    # customer purchase
    sql_str1 = "select A.city as destination, count(A.city) as count from customer_purchase natural join ticket natural join flight, airport as A where arrive_airport_name = A.name and airline_name = %s \
              and (arrival_date between %s and %s) \
              group by A.city order by count(A.city) desc;"
    sql_str2 = "select A.city as destination, count(A.city) as count from customer_purchase natural join ticket natural join flight, airport as A where arrive_airport_name = A.name and airline_name = %s \
              and Year(arrival_date) = YEAR(curdate()) - 1 \
              group by A.city order by count(A.city) desc;"

    # agent purchase
    sql_str3 = "select A.city as destination, count(A.city) as count from agent_purchase natural join ticket natural join flight, airport as A where arrive_airport_name = A.name and airline_name = %s \
              and (arrival_date between %s and %s) \
              group by A.city order by count(A.city) desc;"
    sql_str4 = "select A.city as destination, count(A.city) as count from agent_purchase natural join ticket natural join flight, airport as A where arrive_airport_name = A.name and airline_name = %s \
              and Year(arrival_date) = YEAR(curdate()) - 1 \
              group by A.city order by count(A.city) desc;"
    cursor.execute(sql_str1, (airline_name, three_months_prev, today))
    result1 = cursor.fetchall()

    cursor.execute(sql_str2, airline_name)
    result2 = cursor.fetchall()

    cursor.execute(sql_str3, (airline_name, three_months_prev, today))
    result3 = cursor.fetchall()

    cursor.execute(sql_str4, airline_name)
    result4 = cursor.fetchall()

    # combine results from customer and agent purchase and sort in descending order
    list1 = top_destination_all_list(result1, result3)
    list2 = top_destination_all_list(result2, result4)

    # we only want the top 3 popular destinations
    if len(list1) > 3:
        list1 = list1[:3]
    if len(list2) > 3:
        list2 = list2[:3]
    cursor.close()
    connection.close()
    return render(request, 'staff/view_top_destinations.html', {'list1': list1, 'list2': list2})


@login_check_staff
def view_top_booking_agents(request):
    airline_name = request.session['airline_name']
    cursor = connection.cursor()

    today = dt.date.today()
    delta1 = relativedelta(months=1)
    delta2 = relativedelta(months=12)
    past_month = today - delta1
    past_year = today - delta2

    # past month and past year
    sql_str1 = "select agent_email, COUNT(ticket_id) from agent_purchase natural join ticket where airline_name = %s and (purchase_date between %s and %s) " \
               "group by agent_email order by COUNT(ticket_id) desc LIMIT 5;"

    # last year
    sql_str2 = "select agent_email, SUM(sold_price * 0.1) as amount from agent_purchase natural join ticket " \
               "where airline_name = %s and YEAR(purchase_date) = YEAR(CURDATE()) - 1 group by agent_email order by amount desc LIMIT 5;"

    cursor.execute(sql_str1, (airline_name, past_month, today))
    data1 = cursor.fetchall()

    cursor.execute(sql_str1, (airline_name, past_year, today))
    data2 = cursor.fetchall()

    cursor.execute(sql_str2, airline_name)
    data3 = cursor.fetchall()

    return render(request, 'staff/view_top_booking_agents.html', locals())


@login_check_staff
def revenue_comparison_staff(request):
    airline_name = request.session['airline_name']
    cursor = connection.cursor()

    # last month
    sql_str1 = "select SUM(sold_price) from customer_purchase natural join ticket where airline_name = %s and MONTH(purchase_date) = MONTH(CURDATE()) - 1;"
    sql_str2 = "select SUM(sold_price) from agent_purchase natural join ticket where airline_name = %s and MONTH(purchase_date) = MONTH(CURDATE()) - 1;"
    # last year
    sql_str3 = "select SUM(sold_price) from customer_purchase natural join ticket where airline_name = %s and YEAR(purchase_date) = YEAR(CURDATE()) - 1;"
    sql_str4 = "select SUM(sold_price) from agent_purchase natural join ticket where airline_name = %s and YEAR(purchase_date) = YEAR(CURDATE()) - 1;"

    cursor.execute(sql_str1, airline_name)
    res1 = cursor.fetchall()[0][0]
    cursor.execute(sql_str2, airline_name)
    res2 = cursor.fetchall()[0][0]

    if res1 is None:
        res1 = 0
    if res2 is None:
        res2 = 0

    cursor.execute(sql_str3, airline_name)
    res3 = cursor.fetchall()[0][0]

    cursor.execute(sql_str4, airline_name)
    res4 = cursor.fetchall()[0][0]

    if res3 is None:
        res3 = 0
    if res4 is None:
        res4 = 0

    return render(request, 'staff/compare_revenue.html', locals())


@login_check_staff
def logout_staff(request):
    del request.session['user']
    del request.session['airline_name']
    del request.session['user_type']
    return HttpResponseRedirect(reverse('App:login_staff'))


# agent
@login_check_agent
def agent_index(request):
    cursor = connection.cursor()

    email = request.session['user']

    sql_str = "select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,A.city as Arrival_city,arrive_airport_name,D.city as Depart_city,depart_airport_name, ticket.sold_price " + \
              "from booking_agent natural join agent_purchase natural join ticket natural join flight,airport as A, airport as D " + \
              f"where agent_email = %s and flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name;"
    cursor.execute(sql_str, email)
    flights = cursor.fetchall()
    cursor.close()
    connection.close()

    print('flights: ', flights)

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

        return render(request, 'booking_agent/index.html',
                      {'history_flights': history_flights, 'future_flights': future_flights,
                       'current_flights': current_flight})
    else:
        return render(request, 'booking_agent/index.html',
                      {'message': "You didn't purchase any ticket yet!"})


@login_check_agent
def agent_search(request):
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
                args = (DepartAirport, SourceCity, ArriveAirport, DestinationCity, Depart_date)
                sql_str = "select flight_num,airline_name,depart_date,depart_time,arrival_date,arrival_time,base_price " + \
                          "from flight,airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                          f" and flight.depart_airport_name = %s and D.city = %s and " \
                          f"flight.arrive_airport_name = %s and A.city = %s and depart_date = %s;"
                cursor = connection.cursor()
                cursor.execute(sql_str, args)
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
                args1 = (DepartAirport, SourceCity, ArriveAirport, DestinationCity, Depart_date)
                args2 = (ArriveAirport, DestinationCity, DepartAirport, SourceCity, Return_date)

                sql_str1 = "select flight_num,airline_name,depart_date,depart_time,arrival_date,arrival_time,base_price " + \
                           "from flight,airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                           f" and flight.depart_airport_name = %s and D.city = %s and " \
                           f"flight.arrive_airport_name = %s and A.city = %s and depart_date = %s"

                sql_str2 = "select flight_num,airline_name,depart_date,depart_time,arrival_date,arrival_time,base_price " + \
                           "from flight,airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                           f" and flight.depart_airport_name = %s and D.city = %s and " \
                           f"flight.arrive_airport_name = %s and A.city = %s and depart_date = %s"

                cursor = connection.cursor()

                cursor.execute(sql_str1, args1)
                flight_first = cursor.fetchall()

                cursor.execute(sql_str2, args2)
                flight_second = cursor.fetchall()

                cursor.close()
                connection.close()

                if flight_first and flight_second:
                    print("round trip flight search is successful")
                    return render(request, 'booking_agent/search.html', {'form': form,
                                                                         'sourceCity': SourceCity,
                                                                         'destinationCity': DestinationCity,
                                                                         'flight_first': flight_first,
                                                                         'flight_second': flight_second,
                                                                         'trip_count': 2})
                else:
                    print('cannot find flights')
                    return render(request, 'booking_agent/search.html', {'form': form,
                                                                         'message': 'No flights available!'})
    else:
        form = FlightSearchForm(request.POST)
    return render(request, 'booking_agent/search.html', {'form': form})


@login_check_agent
def agent_purchase(request):
    if request.method == 'POST':
        form = CustomerPurchaseForm(request.POST)
        if form.is_valid():
            agent_email = request.session['user']
            agent_id = request.session['agent_id']

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
            args = (
                agent_email, agent_id, t_id, customer_email, card_type, card_num, name_on_card, expire_at,
                purchase_date,
                purchase_time)
            sql_str1 = f"Insert into agent_purchase(agent_email, agent_id, ticket_id,customer_email,card_type,card_num,name_on_card,expire_at,purchase_date,purchase_time)\
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(sql_str1, args)

            sql_str2 = f"select seats,capacity,ID from ticket natural join flight, airplane \
                        where flight.airplane_id = airplane.ID and ticket.ticket_id = %s"
            cursor.execute(sql_str2, t_id)
            seats, capacity, ID = cursor.fetchall()[0]
            print('seats: ', seats, 'capacity: ', capacity)

            # check seats
            if seats > 0:
                if seats <= capacity * 0.3:
                    # 70% of tickets have been booked, 20 % increase in ticket price
                    print("Sorry we need to increase the ticket price")
                    cursor.execute(
                        "update ticket t set t.sold_price = t.sold_price * 1.2 where t.ticket_id = %s;", t_id)
                # update seats
                cursor.execute(f"update airplane a set a.seats = a.seats - 1 where a.ID = %s;", ID)
                cursor.close()
                connection.close()
                print("Ticket successful purchased!")
                print("Remaining seats are ", seats - 1)
                return HttpResponseRedirect(reverse('App:agent_index'))
            else:
                warning_msg = "Sorry, the airplane has reached its capacity!"
                return render(request, 'booking_agent/purchase.html', locals())
    else:
        form = CustomerPurchaseForm()
    return render(request, 'booking_agent/purchase.html', locals())


@login_check_agent
def agent_commission(request):
    agent_email, agent_id = request.session['user'], request.session['agent_id']
    if request.method == 'GET':
        cursor = connection.cursor()

        today = dt.date.today()
        delta = relativedelta(days=30)
        thirty_days_prev = today - delta

        args = (agent_email, agent_id, thirty_days_prev, today)

        sql_str1 = "select SUM(0.1 * sold_price) as commision from agent_purchase natural join ticket \
                    where agent_email = %s and agent_id = %s \
                    and (purchase_date between %s and %s);"

        sql_str2 = "select AVG(0.1 * sold_price) as commision from agent_purchase natural join ticket \
                            where agent_email = %s and agent_id = %s \
                            and (purchase_date between %s and %s);"

        sql_str3 = "select COUNT(ticket_id) as commision from agent_purchase natural join ticket \
                                    where agent_email = %s and agent_id = %s \
                                    and (purchase_date between %s and %s);"
        cursor.execute(sql_str1, args)
        total_commission = cursor.fetchall()[0][0]

        cursor.execute(sql_str2, args)
        avg_commission = cursor.fetchall()[0][0]

        cursor.execute(sql_str3, args)
        ticket_count = cursor.fetchall()[0][0]
        default = True
        cursor.close()
        connection.close()
        return render(request, 'booking_agent/view_commissions.html', locals())

    elif request.method == 'POST':
        cursor = connection.cursor()
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')

        sql_str1 = "select SUM(0.1 * sold_price) as commission from agent_purchase natural join ticket " \
                   "where agent_email = %s and agent_id = %s and (purchase_date between %s and %s);"

        sql_str2 = "select AVG(0.1 * sold_price) as commission from agent_purchase natural join ticket " \
                   "where agent_email = %s and agent_id = %s and (purchase_date between %s and %s);"

        sql_str3 = "select COUNT(0.1 * sold_price) as commission from agent_purchase natural join ticket " \
                   "where agent_email = %s and agent_id = %s and (purchase_date between %s and %s);"

        args = (agent_email, agent_id, startDate, endDate)

        cursor.execute(sql_str1, args)
        total_commission = cursor.fetchall()[0][0]

        cursor.execute(sql_str2, args)
        avg_commission = cursor.fetchall()[0][0]

        cursor.execute(sql_str3, args)
        ticket_count = cursor.fetchall()[0][0]
        default = False
        cursor.close()
        connection.close()
        return render(request, 'booking_agent/view_commissions.html', locals())


@login_check_agent
def view_top_customers(request):
    agent_email, agent_id = request.session['user'], request.session['agent_id']
    cursor = connection.cursor()

    today = dt.date.today()
    delta = relativedelta(months=6)
    six_months_prev = today - delta

    sql_str1 = "select customer_email, COUNT(ticket_id) from agent_purchase where agent_email = %s and agent_id = %s and (purchase_date between %s and %s) " \
               "group by customer_email order by COUNT(ticket_id) desc LIMIT 5;"

    # last year
    sql_str2 = "select customer_email, SUM(sold_price * 0.1) as amount from agent_purchase natural join ticket " \
               "where agent_email = %s and agent_id = %s and YEAR(purchase_date) = YEAR(CURDATE()) -1 group by customer_email order by amount desc LIMIT 5;"

    cursor.execute(sql_str1, (agent_email, agent_id, six_months_prev, today))
    data1 = cursor.fetchall()

    cursor.execute(sql_str2, (agent_email, agent_id))
    data2 = cursor.fetchall()

    print("top_five_tickets_count: ", data1)
    print("top_five_commission: ", data2)

    return render(request, 'booking_agent/view_top_customers.html', locals())


@login_check_agent
def logout_agent(request):
    del request.session['user']
    del request.session['agent_id']
    return HttpResponseRedirect(reverse('App:login_booking_agent'))
