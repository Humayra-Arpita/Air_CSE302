from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([CustomUser, Category, Location, Property, PropertyImage, Booking, Review, HelpCenter, Contact])
