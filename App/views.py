from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import *
from django.urls import reverse
import hashlib
import datetime


def hashed(pwd):
    return hashlib.sha256(pwd.encode('utf-8')).hexdigest()


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
                flights = Flight.objects.filter(arrive_airport_name=ArriveAirport, depart_airport_name=DepartAirport,
                                                arrive_airport_name__city=DestinationCity,
                                                depart_airport_name__city=SourceCity,
                                                depart_date=Depart_date)
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
                flight_first = Flight.objects.filter(arrive_airport_name=ArriveAirport,
                                                     depart_airport_name=DepartAirport,
                                                     arrive_airport_name__city=DestinationCity,
                                                     depart_airport_name__city=SourceCity,
                                                     depart_date=Depart_date)

                flight_second = Flight.objects.filter(arrive_airport_name=DepartAirport,
                                                      depart_airport_name=ArriveAirport,
                                                      arrive_airport_name__city=SourceCity,
                                                      depart_airport_name__city=DestinationCity,
                                                      depart_date=Return_date)
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

            customer = Customer.objects.create(email=email, name=name, password=hashed_password,
                                               building_num=building_num, street=street, city=city,
                                               state=state, phone_num=phone_num, passport_num=passport_num,
                                               passport_country=passport_country, passport_expire=passport_expire,
                                               date_of_birth=date_of_birth)
            customer.save()

            messages.success(request, f'App Account created for {email}!')
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

            check_email = Customer.objects.filter(email__exact=email)  # check if email exists
            if not check_email:
                return render(request, 'customer/login.html',
                              {'form': form, 'message': "Email address doesn't exist!", 'need_to_signup': True})

            check_matches = Customer.objects.filter(email__exact=email,
                                                    password=hashed_password)  # check if email and password matches
            if check_matches:
                print('log in successfully')
                request.session['user'] = email
                print('session ID: ', request.session['user'])
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
    email = request.session['user']  # get email (pk) from session
    customer = Customer.objects.filter(email__exact=email)
    flights = customer.values('customerpurchase__ticket_id__flight_num',
                              'customerpurchase__ticket_id__airline_name',
                              'customerpurchase__ticket_id__depart_date',
                              'customerpurchase__ticket_id__depart_time',
                              )
    flights = [entry for entry in flights]  # convert the dict to list

    # join 交给前端 此处返回全部flight objects
    extra_info = [
        Flight.objects.filter(flight_num__exact=f['customerpurchase__ticket_id__flight_num']).values('arrival_date',
                                                                                                     'arrival_time',
                                                                                                     'arrive_airport_name',
                                                                                                     'depart_airport_name',
                                                                                                     ) for
        f in flights]
    for i in range(len(extra_info)):
        extra_info[i] = [item for item in extra_info[i]]
    print(extra_info)
    if len(extra_info) > 1:
        for index in range(len(flights)):
            # each flight is a dict
            flights[index]['arrival_date'] = extra_info[index][0]['arrival_date']
            flights[index]['arrival_time'] = extra_info[index][0]['arrival_time']
            flights[index]['arrive_airport_name'] = extra_info[index][0]['arrive_airport_name']
            flights[index]['arrive_airport_name__city'] = Airport.objects.filter(
                name__exact=extra_info[index][0]['arrive_airport_name']).first().city
            flights[index]['depart_airport_name'] = extra_info[index][0]['depart_airport_name']
            flights[index]['depart_airport_name__city'] = Airport.objects.filter(
                name__exact=extra_info[index][0]['depart_airport_name']).first().city
        return render(request, 'customer/index.html',
                      {'customer': customer, 'flights': flights})
    else:
        return render(request, 'customer/index.html',
                      {'customer': customer, 'message': "You didn't purchase any ticket!"})


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
                flights = Flight.objects.filter(arrive_airport_name=ArriveAirport, depart_airport_name=DepartAirport,
                                                arrive_airport_name__city=DestinationCity,
                                                depart_airport_name__city=SourceCity,
                                                depart_date=Depart_date)
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
                flight_first = Flight.objects.filter(arrive_airport_name=ArriveAirport,
                                                     depart_airport_name=DepartAirport,
                                                     arrive_airport_name__city=DestinationCity,
                                                     depart_airport_name__city=SourceCity,
                                                     depart_date=Depart_date)

                flight_second = Flight.objects.filter(arrive_airport_name=DepartAirport,
                                                      depart_airport_name=ArriveAirport,
                                                      arrive_airport_name__city=SourceCity,
                                                      depart_airport_name__city=DestinationCity,
                                                      depart_date=Return_date)
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
            flight_num = form.cleaned_data['flight_num']
            customer_email = form.cleaned_data['email']
            card_type = form.cleaned_data['card_type']
            card_num = form.cleaned_data['card_num']
            name_on_card = form.cleaned_data['name_on_card']
            expire_at = form.cleaned_data['expire_at']
            purchase_date = datetime.date.today()
            purchase_time = datetime.datetime.now().time()
            t_id = helper(flight_num)
            print(t_id)
            cp = CustomerPurchase.objects.create(customer_email=Customer.objects.get(email=customer_email),
                                                 card_type=card_type,
                                                 card_num=card_num,
                                                 name_on_card=name_on_card,
                                                 expire_at=expire_at,
                                                 purchase_date=purchase_date,
                                                 purchase_time=purchase_time,
                                                 ticket_id= Ticket.objects.get(ticket_id=t_id))
            cp.save()
            airplane_id = cp.values('ticket_id__airline_name__airplane_id').first()
            print('airplane_id: ', airplane_id)
            seats = Airplane.objects.filter(airplane_id__exact=airplane_id).first().seats
            print('seats: ', seats)
            seats -= 1
            return render(request, 'customer/purchase.html', locals())

    else:
        form = CustomerPurchaseForm()
    return render(request, 'customer/purchase.html', locals())


def helper(flight_num):
    already_booked = CustomerPurchase.objects.values('ticket_id__ticket_id', 'ticket_id__flight_num')
    ticket_ids_booked = {'ticket_id': []}
    result = ''
    for pair_dict in already_booked:
        if pair_dict['ticket_id__flight_num'] == flight_num:
            ticket_ids_booked['ticket_id'].append(pair_dict['ticket_id__ticket_id'])
    print(ticket_ids_booked)

    all_ticket_ids = Ticket.objects.filter(flight_num=flight_num).values('ticket_id')
    print(all_ticket_ids)
    for t_id in all_ticket_ids:
        if t_id not in ticket_ids_booked['ticket_id']:
            result = t_id['ticket_id']
            break
    return result
