from django.db import models


class Customer(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    building_num = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=30)
    passport_num = models.CharField(max_length=20)
    passport_country = models.CharField(max_length=30)
    passport_expire = models.DateField(max_length=50)
    date_of_birth = models.DateTimeField()

    class Meta:
        db_table = 'customer'


class AgentPurchase(models.Model):
    ticket_id = models.OneToOneField('Ticket', on_delete=models.CASCADE,
                                     primary_key=True)  # unique
    customer_email = models.ForeignKey('Customer', on_delete=models.CASCADE)  # one to one
    agent_email = models.ForeignKey('BookingAgent', on_delete=models.CASCADE,
                                    related_name="agent-purchase+", to_field='agent_email')  # many to one
    agent_id = models.ForeignKey('BookingAgent', on_delete=models.CASCADE, related_name="agent-purchase+",
                                 to_field='agent_id')  # many to one

    card_type = models.CharField(max_length=30)
    card_num = models.CharField(max_length=30)
    name_on_card = models.CharField(max_length=30)
    expire_at = models.DateField()
    purchase_date = models.DateField()
    purchase_time = models.TimeField()

    class Meta:
        db_table = 'agent_purchase'


class Airline(models.Model):
    airline_name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        db_table = 'airline'


class Airplane(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=30)  # Field name made lowercase.
    airline_name = models.ForeignKey(Airline, on_delete=models.CASCADE,
                                     to_field='airline_name')
    seats = models.IntegerField()
    capacity = models.IntegerField()

    class Meta:
        db_table = 'airplane'


class Airport(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    city = models.CharField(max_length=50)

    class Meta:
        db_table = 'airport'


class BookingAgent(models.Model):
    agent_email = models.CharField(primary_key=True, max_length=50)
    agent_id = models.CharField(max_length=30, unique=True)
    agent_password = models.CharField(max_length=255)

    class Meta:
        db_table = 'booking_agent'


class CustomerPurchase(models.Model):
    ticket_id = models.OneToOneField('Ticket', on_delete=models.CASCADE, db_column='ticket_id', primary_key=True)
    customer_email = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='email')
    card_type = models.CharField(max_length=30)
    card_num = models.CharField(max_length=30)
    name_on_card = models.CharField(max_length=30)
    expire_at = models.CharField(max_length=50)
    purchase_date = models.DateField()
    purchase_time = models.TimeField()

    class Meta:
        db_table = 'customer_purchase'


class Flight(models.Model):
    flight_iid = models.AutoField(primary_key=True)

    flight_num = models.CharField(max_length=50)
    depart_date = models.DateField()
    depart_time = models.TimeField()
    airline_name = models.ForeignKey(Airline, on_delete=models.CASCADE,
                                     to_field='airline_name')
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    airplane_id = models.ForeignKey(Airplane, on_delete=models.CASCADE, to_field='id')
    base_price = models.CharField(max_length=11)
    status = models.CharField(max_length=11)
    arrive_airport_name = models.ForeignKey(Airport, on_delete=models.CASCADE,
                                            to_field='name',
                                            related_name="flight+")
    depart_airport_name = models.ForeignKey(Airport, on_delete=models.CASCADE,
                                            to_field='name',
                                            related_name="flight+")

    class Meta:
        db_table = 'flight'
        constraints = [
            models.UniqueConstraint(fields=['flight_num', 'airline_name', 'depart_date', 'depart_time'],
                                    name='flight_unique')
        ]


class PhoneNum(models.Model):
    # each username only has one phone number
    username = models.OneToOneField('Staff', on_delete=models.CASCADE, db_column='username', primary_key=True)
    number = models.CharField(max_length=30)

    class Meta:
        db_table = 'phone_num'


class Rate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, primary_key=True, db_column='created_at')
    customer_email = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                       related_name='rate_customer_email', to_field='email')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='rate_flight')
    # airline_name = models.ForeignKey(Flight, on_delete=models.CASCADE, db_column='airline_name', related_name="rate+")
    # flight_num = models.ForeignKey(Flight, on_delete=models.CASCADE, db_column='flight_num', related_name="rate+")
    # depart_date = models.ForeignKey(Flight, on_delete=models.CASCADE, db_column='depart_date', related_name="rate+")
    # depart_time = models.ForeignKey(Flight, on_delete=models.CASCADE, db_column='depart_time', related_name="rate+")
    comment = models.CharField(max_length=255, blank=True, null=True)
    ratings = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'rate'


class Staff(models.Model):
    username = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=255)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    airline_name = models.ForeignKey(Airline, on_delete=models.CASCADE, db_column='airline_name')

    class Meta:
        db_table = 'staff'


class Ticket(models.Model):
    ticket_id = models.CharField(primary_key=True, max_length=11)
    sold_price = models.CharField(max_length=11)
    t_flight_iid = models.ForeignKey(Flight, on_delete=models.CASCADE,
                                     db_column='t_flight_iid', related_name="ticket_flight")

    # t_airline_name = models.ForeignKey(Flight, on_delete=models.CASCADE,
    #                                    db_column='airline_name', related_name="ticket_airline_name",
    #                                    to_field='airline_name')
    # t_flight_num = models.ForeignKey(Flight, on_delete=models.CASCADE, db_column='flight_num',
    #                                  related_name="ticket_flight_num", to_field='flight_num')
    # t_depart_date = models.ForeignKey(Flight, on_delete=models.CASCADE, db_column='depart_date',
    #                                   related_name="ticket_depart_date", to_field='depart_date')
    # t_depart_time = models.ForeignKey(Flight, on_delete=models.CASCADE, db_column='depart_time',
    #                                   related_name="ticket_depart_time", to_field='depart_time')

    class Meta:
        db_table = 'ticket'
