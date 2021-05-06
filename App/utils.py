import hashlib
import datetime as dt
import time
import shortuuid
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse


def hashed(pwd):
    return hashlib.sha256(pwd.encode('utf-8')).hexdigest()


def generate_ticket_id(flight_num):
    cursor = connection.cursor()
    sql_str1 = "select ticket_id,flight_num from customer_purchase natural join ticket natural join flight"
    sql_str2 = "select ticket_id,flight_num from agent_purchase natural join ticket natural join flight"

    cursor.execute(sql_str1)
    already_booked_cp = cursor.fetchall()

    cursor.execute(sql_str2)
    already_booked_ap = cursor.fetchall()

    ticket_ids_booked = {'ticket_id': []}
    result = ''

    already_booked = already_booked_ap + already_booked_cp

    print('already_booked: ', already_booked)

    for pair in already_booked:
        if pair[1] == flight_num:
            ticket_ids_booked['ticket_id'].append(pair[0])
    print('ticket_ids_booked: ', ticket_ids_booked)

    sql_str3 = f"select ticket_id from ticket natural join flight where flight_num = '{flight_num}'"
    cursor.execute(sql_str3)
    all_ticket_ids = cursor.fetchall()

    print('all_ticket_ids: ', all_ticket_ids)

    for t_id in all_ticket_ids:
        if t_id[0] not in ticket_ids_booked['ticket_id']:
            result = t_id[0]
            break
    cursor.close()
    connection.close()
    return result


def previous_than_today(date, t):
    datetimeobj = dt.datetime.combine(date, t)
    today = dt.datetime.now()
    return datetimeobj < today


def later_than_today(date, t):
    datetimeobj = dt.datetime.combine(date, t)
    today = dt.datetime.now()
    return datetimeobj > today


def before_next_days(date, t, n):
    datetimeobj = dt.datetime.combine(date, t)
    if n > 0:
        today = dt.datetime.now()
        target = today + dt.timedelta(days=n)
        return datetimeobj < target


def correct_month_abbreviate(month):
    lst = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for m in lst:
        if m in month:
            return m


def convert_str_to_date(d):
    if '.' in d:
        index = d.index('.')
        new = correct_month_abbreviate(d[:index])
        d = new + d[index + 1:]

    try:
        converted_date = dt.datetime.strptime(d, "%B %d, %Y").date()
    except ValueError:
        converted_date = dt.datetime.strptime(d, "%b %d, %Y").date()
    return converted_date


def convert_str_to_date_YYYYMMDD(d):
    return dt.datetime.strptime(d, "%Y-%m-%d").date()


def convert_str_to_time(t):
    if 'noon' in t:
        return "12:00:00"
    if ':' not in t:
        tt = t[:2]
        if 'p' in t:
            tt += 'PM'
        else:
            tt += 'AM'
        converted_time = dt.datetime.strptime(tt, "%I %p").time()
    else:
        tt = t[:-4]
        if t[-4:] == 'p.m.':
            tt += 'PM'
        else:
            tt += 'AM'
        converted_time = dt.datetime.strptime(tt, "%I:%M %p").time()
    return converted_time


def convert_to_month(val):
    if val == 1:
        return "Jan"
    if val == 2:
        return "Feb"
    if val == 3:
        return "Mar"
    if val == 4:
        return "Apr"
    if val == 5:
        return "May"
    if val == 6:
        return "Jun"
    if val == 7:
        return "Jul"
    if val == 8:
        return "Aug"
    if val == 9:
        return "Sep"
    if val == 10:
        return "Oct"
    if val == 11:
        return "Nov"
    if val == 12:
        return "Dec"


def login_check_customer(func):
    def wrapper(request, *args, **kwargs):
        try:
            request.session['user']
        except KeyError:
            return HttpResponseRedirect(reverse('App:login_customer'))
        return func(request, *args, **kwargs)

    return wrapper


def login_check_staff(func):
    def wrapper(request, *args, **kwargs):
        try:
            request.session['user']
        except KeyError:
            return HttpResponseRedirect(reverse('App:login_staff'))
        return func(request, *args, **kwargs)

    return wrapper


def login_check_agent(func):
    def wrapper(request, *args, **kwargs):
        try:
            request.session['user']
        except KeyError:
            return HttpResponseRedirect(reverse('App:login_booking_agent'))
        return func(request, *args, **kwargs)

    return wrapper


def top_destination_all_list(c_list, a_list):
    mapp = {}
    for item in c_list:
        mapp[item[0]] = item[1]

    if len(a_list) > 0:
        for item in a_list:
            if item[0] not in mapp:
                mapp[item[0]] = item[1]
            else:
                mapp[item[0]] += item[1]

    res = sorted(mapp.items(), key=lambda x: x[1], reverse=True)
    return res


def create_tickets(sold_price, airline_name, flight_num, depart_date, depart_time, capacity):
    cursor = connection.cursor()
    sql_str = "INSERT INTO ticket(ticket_id, sold_price, airline_name, flight_num, depart_date, depart_time) VALUES(%s, %s, %s, %s, %s, %s);"

    param = []
    t_ids = {'id': []}
    for i in range(capacity):
        t_id = shortuuid.ShortUUID().random(length=22)
        if t_id not in t_ids['id']:
            print(t_id)
            t_ids['id'].append(t_id)
            param.append([t_id, sold_price, airline_name, flight_num, depart_date, depart_time])
            time.sleep(0.001)
        else:
            continue
    try:
        cursor.executemany(sql_str, param)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e)
        cursor.close()
        connection.close()
