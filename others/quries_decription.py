"""Public Info Page"""
# search for flights and view them
sql_str = "select flight.airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time, flight.status " + \
          " from flight, airplane, airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
          " and flight.depart_airport_name = %s and D.city = %s and flight.airline_name = airplane.airline_name and flight.airplane_id = airplane.ID and airplane.seats > 0 and " \
          "flight.arrive_airport_name = %s and A.city = %s and depart_date = %s "

'''customer register'''
sql_str = "Insert into customer(email,name,password,building_num,street,city,state,phone_num,passport_num,passport_country,passport_expire,date_of_birth) " + \
          "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

"""staff register"""
sql_str = "Insert into staff(username,password,f_name,l_name,date_of_birth,airline_name) values \
            (%s, %s, %s, %s, %s, %s);"

"""booking agent register"""
sql_str = "Insert into booking_agent(agent_email, agent_id, agent_password) VALUES(%s, %s, %s);"

"""customer login"""
sql_str = "select email from customer where email = %s;"  # check if email exists
sql_str = "select email from customer where email = %s and password = %s;"  # check if email and password are correct

"""# staff login"""
sql_str = "select * from staff where username = %s;"  # check if user exists
sql_str = "select airline_name from staff where username = %s and password = %s;"  # check if username and password are correct

"""# booking agent login"""
sql_str = "select * from booking_agent where agent_email = %s;"  # check if agent_email exists
sql_str = "select * from booking_agent where agent_email = %s and agent_password = %s and agent_id = %s;"  # check if email and passwords are correct

"""# customer index page"""
# show customer purchase flight information, including history flights, current flights, and future flights
sql_str = "SELECT airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,A.city as Arrival_city,arrive_airport_name,D.city as Depart_city,depart_airport_name, ticket.sold_price,flight.status " + \
                  "from customer, customer_purchase natural join ticket natural join flight,airport as A, airport as D " + \
                  "where customer.email = customer_purchase.customer_email and email = %s and flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name;"

# show customer purchase flight information based on user input (source/destination city, airport, startdate, enddate)
sql_str = "SELECT airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,A.city,arrive_airport_name,D.city,depart_airport_name, sold_price, flight.status " + \
                  "from customer, customer_purchase natural join ticket natural join flight,airport as A, airport as D " + \
                  "where customer.email = customer_purchase.customer_email and email = %s and flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name " \
                  "and (depart_date between %s and %s) and D.city = %s and D.name = %s and A.city = %s and A.name = %s;"

"""# customer search"""
sql_str = "select flight_num, flight.airline_name,depart_date,depart_time,arrival_date,arrival_time,base_price,flight.status " + \
                      "from flight,airplane, airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
                      " and flight.depart_airport_name = %s and D.city = %s and flight.airline_name = airplane.airline_name and flight.airplane_id = airplane.ID and airplane.seats > 0 and " \
                      "flight.arrive_airport_name = %s and A.city = %s and depart_date = %s;"

"""# customer purchase"""

# purchase form
sql_str = "Insert into customer_purchase(customer_email,ticket_id,card_type,card_num,name_on_card,expire_at,purchase_date,purchase_time) \
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"

# check seats, capacity and airplane ID
sql_str1 = "select seats,capacity,ID from ticket natural join flight, airplane \
            where flight.airplane_id = airplane.ID and ticket.ticket_id = %s;"

# update ticket price
sql_str2 = "update ticket t set t.sold_price = t.sold_price * 1.2 where t.ticket_id = %s;"

# update seats
sql_str3 = "update airplane a set a.seats = a.seats - 1 where a.ID = %s;"

"""customer comment"""
sql_str = "Insert into rate(customer_email,airline_name,flight_num,depart_date,depart_time,comment,rating) " + \
          "VALUES(%s,%s,%s,%s,%s,%s,%s);"

"""agent index page"""
# show history flights, current flights and future flights
sql_str = "select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,A.city,A.name,D.city,D.name, sold_price, customer_email,flight.status " + \
                  " from booking_agent natural join agent_purchase natural join ticket natural join flight,airport as A, airport as D " + \
                  " where agent_email = %s and flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name;"


"""agent search """
sql_str = "select flight_num,flight.airline_name,depart_date,depart_time,arrival_date,arrival_time,base_price,flight.status " + \
          "from flight,airplane, airport as D, airport as A where flight.arrive_airport_name = A.name and flight.depart_airport_name = D.name" + \
          " and flight.depart_airport_name = %s and D.city = %s and flight.airline_name = airplane.airline_name and flight.airplane_id = airplane.ID and airplane.seats > 0 and " \
          " flight.arrive_airport_name = %s and A.city = %s and depart_date = %s;"

"""agent purchase"""
# purchase form
sql_str1 = "Insert into agent_purchase(agent_email, agent_id, ticket_id,customer_email,card_type,card_num,name_on_card,expire_at,purchase_date,purchase_time)\
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
# check seats, capacity and airplane ID
sql_str2 = "select seats,capacity,ID from ticket natural join flight, airplane \
            where flight.airplane_id = airplane.ID and ticket.ticket_id = %s"

# update ticket price
sql_str2 = "update ticket t set t.sold_price = t.sold_price * 1.2 where t.ticket_id = %s;"

# update seats
sql_str3 = "update airplane a set a.seats = a.seats - 1 where a.ID = %s;"

"""agent commission"""
# view total commission in the past 30 days
sql_str1 = "select SUM(0.1 * sold_price) as commision from agent_purchase natural join ticket \
                    where agent_email = %s and agent_id = %s \
                    and (purchase_date between %s and %s);"

# view average commission in the past 30 days
sql_str2 = "select AVG(0.1 * sold_price) as commision from agent_purchase natural join ticket \
                    where agent_email = %s and agent_id = %s \
                    and (purchase_date between %s and %s);"

# view number of tickets sold by the agent in the past 30 days
sql_str3 = "select COUNT(ticket_id) as commision from agent_purchase natural join ticket \
                            where agent_email = %s and agent_id = %s \
                            and (purchase_date between %s and %s);"

"""view top customers"""
# top 5 customers based on number of tickets bought in the past 6 months from booking agent
sql_str1 = "select customer_email, COUNT(ticket_id) from agent_purchase where agent_email = %s and agent_id = %s and (purchase_date between %s and %s) " \
           "group by customer_email order by COUNT(ticket_id) desc LIMIT 5;"
# top 5 customers based on amount of commission received int he last year from booking agent
sql_str2 = "select customer_email, SUM(sold_price * 0.1) as amount from agent_purchase natural join ticket " \
               "where agent_email = %s and agent_id = %s and YEAR(purchase_date) = YEAR(CURDATE()) -1 group by customer_email order by amount desc LIMIT 5;"

"""staff index page"""
# default
sql_str = "select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,status,A.city as Arrival_city,arrive_airport_name as arrive_airport,D.city as Depart_city,depart_airport_name as depart_airport,flight.status \
             from flight,airport as D,airport as A where airline_name = %s and flight.arrive_airport_name = A.name \
             and flight.depart_airport_name = D.name"
# based on user input on ranges of dates, source/destination airport, cities
sql_str = "select airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,status,A.city as Arrival_city,arrive_airport_name as arrive_airport,D.city as Depart_city,depart_airport_name as depart_airport, flight.status \
         from flight,airport as D,airport as A where airline_name = %s and flight.arrive_airport_name = A.name \
      and flight.depart_airport_name = D.name and D.city = %s and depart_airport_name = %s and A.city = %s and arrive_airport_name = %s \
      and (depart_date between %s and %s);"

"""view customers"""
# view customers from customer-purchase
sql_str1 = "select c.name, c.email from flight natural join ticket natural join customer_purchase as cp,customer as c where " \
           "cp.customer_email = c.email and flight.flight_num = %s and flight.depart_date = %s and flight.depart_time = %s and flight.airline_name = %s"
# view customers from agent_purchase
sql_str2 = "select c.name, c.email from flight natural join ticket natural join agent_purchase as ap, customer as c where " \
           "ap.customer_email = c.email and flight.flight_num = %s and flight.depart_date = %s and flight.depart_time = %s and flight.airline_name = %s"

"""view most frequent customers"""
sql_str = "select customer_email,count(*) from ticket natural join customer_purchase where airline_name=%s and YEAR(purchase_date) = YEAR(CURDATE()) - 1 group by customer_email order by count(*) desc limit 5"

"""view all flights taken by one customer"""
sql_str = "select flight_num, depart_date, depart_time, depart_airport_name, arrive_airport_name from flight natural join ticket natural join customer_purchase as cp, customer c where cp.customer_email = c.email and airline_name = %s and c.email = %s order by depart_date, depart_time;"

"""create new flight"""
sql_str1 = "select distinct ID from airplane where airline_name = %s" # get airplane ids
sql_str2 = "select name from airport" # get all airport names
sql_str3 = "select capacity from airplane where airline_name = %s and ID = %s" # get capacity of a certain airplane

# create new flight
sql_str = "Insert into flight(airline_name,flight_num,depart_date,depart_time,arrival_date,arrival_time,airplane_id,base_price,status,arrive_airport_name,depart_airport_name)" \
          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

"""change flight status"""
sql_str = "UPDATE flight t SET t.status = %s WHERE t.airline_name = %s and t.flight_num = %s and t.depart_date = %s and t.depart_time = %s;"

"""add airplane in the system"""
sql_str = "INSERT INTO airplane(ID,airline_name,seats,capacity) VALUES(%s, %s, %s, %s)"

"""add airport"""
sql_str = "INSERT INTO airport(name,city) VALUES(%s, %s)"

"""view flight ratings"""
# average rating, all comments, ratings, and their creation timestamp
sql_str1 = "select AVG(rating) from rate natural join flight where airline_name = %s and flight_num = %s and depart_date = %s and depart_time = %s"
sql_str2 = "select comment,rating,created_at from rate natural join flight where airline_name = %s and flight_num = %s and depart_date = %s and depart_time = %s"

"""view top 5 booking agents"""
# past month and past year
sql_str1 = "select agent_email, COUNT(ticket_id) from agent_purchase natural join ticket where airline_name = %s and (purchase_date between %s and %s) " \
           "group by agent_email order by COUNT(ticket_id) desc LIMIT 5;"

# last year
sql_str2 = "select agent_email, SUM(sold_price * 0.1) as amount from agent_purchase natural join ticket " \
           "where airline_name = %s and YEAR(purchase_date) = YEAR(CURDATE()) - 1 group by agent_email order by amount desc LIMIT 5;"

"""view reports"""
# customer purchase

# total amount of tickets sold from customer purchase
sql_str1 = "select SUM(sold_price) from customer_purchase natural join ticket \
            where airline_name = %s and (purchase_date between %s and %s);"
# month wise show
sql_str2 = "select MONTH(purchase_date), SUM(sold_price) from customer_purchase natural join ticket \
                       where airline_name = %s and (purchase_date between %s and %s) \
                        group by MONTH(purchase_date) order by MONTH(purchase_date);"

# total amount of tickets sold from agent_purchase
sql_str3 = "select SUM(sold_price) from agent_purchase natural join ticket \
            where airline_name = %s and (purchase_date between %s and %s);"
# month wise show
sql_str4 = "select MONTH(purchase_date), SUM(sold_price) from agent_purchase natural join ticket \
                       where airline_name = %s and (purchase_date between %s and %s) \
                        group by MONTH(purchase_date) order by MONTH(purchase_date);"

"""Comparison of Revenue earned"""
# last month
# customer purchase
sql_str1 = "select SUM(sold_price) from customer_purchase natural join ticket where airline_name = %s and MONTH(purchase_date) = MONTH(CURDATE()) - 1;"
# agent purchase
sql_str2 = "select SUM(sold_price) from agent_purchase natural join ticket where airline_name = %s and MONTH(purchase_date) = MONTH(CURDATE()) - 1;"

# last year
# customer purchase
sql_str3 = "select SUM(sold_price) from customer_purchase natural join ticket where airline_name = %s and YEAR(purchase_date) = YEAR(CURDATE()) - 1;"
# agent purchase
sql_str4 = "select SUM(sold_price) from agent_purchase natural join ticket where airline_name = %s and YEAR(purchase_date) = YEAR(CURDATE()) - 1;"

"""view top destinations"""
# customer purchase last 3 months and last year
sql_str1 = "select A.city as destination, count(A.city) as count from customer_purchase natural join ticket natural join flight, airport as A where arrive_airport_name = A.name and airline_name = %s \
          and (arrival_date between %s and %s) \
          group by A.city order by count(A.city) desc;"
sql_str2 = "select A.city as destination, count(A.city) as count from customer_purchase natural join ticket natural join flight, airport as A where arrive_airport_name = A.name and airline_name = %s \
          and Year(arrival_date) = YEAR(curdate()) - 1 \
          group by A.city order by count(A.city) desc;"

# agent purchase last 3 months and last year
sql_str3 = "select A.city as destination, count(A.city) as count from agent_purchase natural join ticket natural join flight, airport as A where arrive_airport_name = A.name and airline_name = %s \
          and (arrival_date between %s and %s) \
          group by A.city order by count(A.city) desc;"
sql_str4 = "select A.city as destination, count(A.city) as count from agent_purchase natural join ticket natural join flight, airport as A where arrive_airport_name = A.name and airline_name = %s \
          and Year(arrival_date) = YEAR(curdate()) - 1 \
          group by A.city order by count(A.city) desc;"
