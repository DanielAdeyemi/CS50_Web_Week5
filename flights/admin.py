from django.contrib import admin
from .models import Flight, Airport

admin.site.register(Airport)
admin.site.register(Flight)
