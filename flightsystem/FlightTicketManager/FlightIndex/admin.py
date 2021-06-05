from django.contrib import admin
from FlightIndex.models import Flight,Airport

# Register your models here.
admin.site.register([Flight,Airport])