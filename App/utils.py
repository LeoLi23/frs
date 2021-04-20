import hashlib
from .models import *
import datetime as dt
from django.db import connection


def hashed(pwd):
    return hashlib.sha256(pwd.encode('utf-8')).hexdigest()


def generate_ticket_id(flight_num):
    cursor = connection.cursor()
    sql_str1 = "select ticket_id,flight_num from customer_purchase natural join ticket natural join flight"
    cursor.execute(sql_str1)
    already_booked = cursor.fetchall()
    # already_booked = CustomerPurchase.objects.values('ticket_id__ticket_id', 'ticket_id__flight_num')
    ticket_ids_booked = {'ticket_id': []}
    result = ''
    for pair in already_booked:
        if pair[1] == flight_num:
            ticket_ids_booked['ticket_id'].append(pair[0])

    print('ticket_ids_booked: ', ticket_ids_booked)
    print(flight_num)

    sql_str2 = f"select ticket_id from ticket natural join flight where flight_num = '{flight_num}'"
    cursor.execute(sql_str2)
    all_ticket_ids = cursor.fetchall()

    print('all_ticket_ids: ', all_ticket_ids)

    for t_id in all_ticket_ids:
        if t_id[0] not in ticket_ids_booked['ticket_id']:
            result = t_id[0]
            break
    cursor.close()
    connection.close()
    return result


def previous_than_today(date, time):
    datetimeobj = dt.datetime.combine(date, time)
    today = dt.datetime.now()
    return datetimeobj < today


def convert_str_to_date(d):
    converted_date = dt.datetime.strptime(d, "%B %d, %Y").date()
    return converted_date


def convert_str_to_time(t):
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
        return "June"
    if val == 7:
        return "July"
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
