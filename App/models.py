# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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
        managed = True
        db_table = 'customer'


class AgentPurchase(models.Model):
    ticket_id = models.OneToOneField('Ticket', on_delete=models.CASCADE, db_column='ticket_id',
                                     primary_key=True)  # unique
    customer_email = models.ForeignKey('Customer', on_delete=models.CASCADE,
                                       db_column='customer_email')  # one to one
    agent_email = models.ForeignKey('BookingAgent', on_delete=models.CASCADE, db_column='agent_email',
                                    related_name="agent-purchase+", to_field='agent_email')  # many to one
    agent_id = models.ForeignKey('BookingAgent', on_delete=models.CASCADE, related_name="agent-purchase+",
                                 db_column='agent_id', to_field='agent_id')  # many to one

    card_type = models.CharField(max_length=30)
    card_num = models.CharField(max_length=30)
    name_on_card = models.CharField(max_length=30)
    expire_at = models.DateField()
    purchase_date = models.DateField()
    purchase_time = models.TimeField()

    class Meta:
        managed = True
        db_table = 'agent_purchase'


class Airline(models.Model):
    airline_name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'airline'


class Airplane(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=30)  # Field name made lowercase.
    airline_name = models.ForeignKey(Airline, on_delete=models.CASCADE, db_column='airline_name')
    seats = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'airplane'
        unique_together = (('id', 'airline_name'),)


class Airport(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    city = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'airport'


class BookingAgent(models.Model):
    agent_email = models.CharField(primary_key=True, max_length=50)
    agent_id = models.CharField(max_length=30, unique=True)
    agent_password = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'booking_agent'
        unique_together = (('agent_email', 'agent_id'),)


class CustomerPurchase(models.Model):
    ticket_id = models.OneToOneField('Ticket', on_delete=models.CASCADE, db_column='ticket_id', primary_key=True)
    customer_email = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='customer_email')
    card_type = models.CharField(max_length=30)
    card_num = models.CharField(max_length=30)
    name_on_card = models.CharField(max_length=30)
    expire_at = models.CharField(max_length=50)
    purchase_date = models.DateField()
    purchase_time = models.TimeField()

    class Meta:
        managed = True
        db_table = 'customer_purchase'


class Flight(models.Model):
    airline_name = models.OneToOneField(Airline, on_delete=models.CASCADE, db_column='airline_name', primary_key=True)
    flight_num = models.CharField(max_length=30, unique=True)
    depart_date = models.DateField(unique=True)
    depart_time = models.TimeField(unique=True)
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    airplane_id = models.ForeignKey(Airplane, on_delete=models.CASCADE, db_column='airplane_id')
    base_price = models.CharField(max_length=11)
    status = models.CharField(max_length=11)
    arrive_airport_name = models.ForeignKey(Airport, on_delete=models.CASCADE, db_column='arrive_airport_name',
                                            related_name="flight+", to_field='name')
    depart_airport_name = models.ForeignKey(Airport, on_delete=models.CASCADE, db_column='depart_airport_name',
                                            related_name="flight+", to_field='name')

    class Meta:
        managed = True
        db_table = 'flight'
        unique_together = (('airline_name', 'flight_num', 'depart_date', 'depart_time'),)


class PhoneNum(models.Model):
    username = models.OneToOneField('Staff', on_delete=models.CASCADE, db_column='username', primary_key=True)
    number = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'phone_num'
        unique_together = (('username', 'number'),)


class Rate(models.Model):
    customer_email = models.OneToOneField(Customer, on_delete=models.CASCADE, db_column='customer_email',
                                          primary_key=True)
    airline_name = models.ForeignKey(Flight, on_delete=models.CASCADE, db_column='airline_name', related_name="rate+",
                                     to_field='airline_name')
    flight_num = models.ForeignKey(Flight, on_delete=models.CASCADE, db_column='flight_num', to_field='flight_num',
                                   related_name="rate+")
    depart_date = models.ForeignKey(Flight, on_delete=models.CASCADE, db_column='depart_date', to_field='depart_date',
                                    related_name="rate+")
    depart_time = models.ForeignKey(Flight, on_delete=models.CASCADE, db_column='depart_time', to_field='depart_time',
                                    related_name="rate+")
    comment = models.CharField(max_length=255, blank=True, null=True)
    ratings = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rate'
        unique_together = (('customer_email', 'airline_name', 'flight_num', 'depart_time', 'depart_date'),)


class Staff(models.Model):
    username = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=255)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    airline_name = models.ForeignKey(Airline, on_delete=models.CASCADE, db_column='airline_name')

    class Meta:
        managed = True
        db_table = 'staff'


class Ticket(models.Model):
    ticket_id = models.CharField(primary_key=True, max_length=11)
    sold_price = models.CharField(max_length=11)
    airline_name = models.ForeignKey(Flight, on_delete=models.CASCADE, to_field='airline_name',
                                     db_column='airline_name', related_name="Ticket+")
    flight_num = models.ForeignKey(Flight, on_delete=models.CASCADE, to_field='flight_num', db_column='flight_num',
                                   related_name="Ticket+")
    depart_date = models.ForeignKey(Flight, on_delete=models.CASCADE, to_field='depart_date', db_column='depart_date',
                                    related_name="Ticket+")
    depart_time = models.ForeignKey(Flight, on_delete=models.CASCADE, to_field='depart_time', db_column='depart_time',
                                    related_name="Ticket+")

    class Meta:
        managed = True
        db_table = 'ticket'
