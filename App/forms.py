from django import forms
from django.db import connection
import re


def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.'?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)


class CustomerRegisterForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput())
    name = forms.CharField(label='Username', max_length=50)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput())
    building_num = forms.CharField(max_length=10)
    street = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    phone_num = forms.CharField(max_length=30)
    passport_num = forms.CharField(max_length=20)
    passport_country = forms.CharField(max_length=30)
    passport_expire = forms.DateField(label='passport_expire', widget=forms.DateInput())
    date_of_birth = forms.DateField(label='date_of_birth', widget=forms.DateInput())

    def clean_username(self):
        name = self.cleaned_data.get('name')

        if len(name) < 3:
            raise forms.ValidationError("your name must be at least 3 characters log")
        elif len(name) > 20:
            raise forms.ValidationError("your name is too long")
        else:
            cursor = connection.cursor()
            cursor.execute(f"select * from customer where name = '{name}'")
            filter_result = cursor.fetchall()
            cursor.close()
            connection.close()
            if len(filter_result) > 0:
                raise forms.ValidationError('your name already exists')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email_check(email):
            cursor = connection.cursor()
            cursor.execute(f"select * from customer where email = '{email}'")
            filter_result = cursor.fetchall()
            cursor.close()
            connection.close()
            if len(filter_result) > 0:
                raise forms.ValidationError("your email already exists")
        else:
            raise forms.ValidationError("Please enter a valid email")

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 3:
            raise forms.ValidationError("your password is too short")
        elif len(password1) > 20:
            raise forms.ValidationError("your password is too long")

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password mismatch Please enter again')

        return password2


class StaffRegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput())
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput())
    f_name = forms.CharField(max_length=30)
    l_name = forms.CharField(max_length=30)
    date_of_birth = forms.DateField(label='date_of_birth', widget=forms.DateInput())
    airline_name = forms.CharField(max_length=255)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("your username must be at least 3 characters log")
        elif len(username) > 20:
            raise forms.ValidationError("your username is too long")
        else:
            cursor = connection.cursor()
            cursor.execute(f"select * from staff where username = '{username}'")
            filter_result = cursor.fetchall()
            cursor.close()
            connection.close()
            if len(filter_result) > 0:
                raise forms.ValidationError('your username already exists')
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 3:
            raise forms.ValidationError("your password is too short")
        elif len(password1) > 20:
            raise forms.ValidationError("your password is too long")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password mismatch Please enter again')

        return password2

    def check_airline_name(self):
        airline_name = self.cleaned_data.get('airline_name')
        cursor = connection.cursor()
        cursor.execute(f"select airline_name from airline where airline_name = '{airline_name}'")
        filter_result = cursor.fetchall()
        cursor.close()
        connection.close()
        if len(filter_result) == 0:
            # this airline name doesn't exist
            print("this airline doesn't exist")
            raise forms.ValidationError("Airline doesn't exist!")
        return airline_name


class BookingAgentRegisterForm(forms.Form):
    agent_email = forms.EmailField(label='Email', widget=forms.TextInput())
    agent_id = forms.CharField(max_length=30)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput())

    def clean_email(self):
        agent_email = self.cleaned_data.get('agent_email')
        if email_check(agent_email):
            cursor = connection.cursor()
            cursor.execute(f"select * from booking_agent where agent_email = '{agent_email}'")
            filter_result = cursor.fetchall()
            cursor.close()
            connection.close()
            if len(filter_result) > 0:
                raise forms.ValidationError("your agent_email already exists")
        else:
            raise forms.ValidationError("Please enter a valid agent_email")

        return agent_email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 3:
            raise forms.ValidationError("your password is too short")
        elif len(password1) > 20:
            raise forms.ValidationError("your password is too long")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password mismatch Please enter again')

        return password2


class CustomerLoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


class BookingAgentLoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


class StaffLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


class FlightSearchForm(forms.Form):
    SourceCity = forms.CharField(label='SourceCity')
    DepartAirport = forms.CharField(label='DepartAirport')
    DestinationCity = forms.CharField(label='DestinationCity')
    ArriveAirport = forms.CharField(label='ArriveAirport')
    Depart_date = forms.DateField(label='Depart_date')
    Return_date = forms.DateField(label='Return_date', required=False)


class CustomerPurchaseForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50)
    card_type = forms.ChoiceField(choices=(("Debit", "Debit"), ("Credit", "Credit")))
    card_num = forms.CharField()
    name_on_card = forms.CharField()
    expire_at = forms.DateField()

