from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Airline)
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(BookingAgent)
admin.site.register(CustomerPurchase)
admin.site.register(AgentPurchase)
