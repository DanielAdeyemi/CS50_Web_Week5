from django.contrib import admin
from .models import Flight, Airport, Passenger

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)
