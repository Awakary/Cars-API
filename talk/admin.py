from django.contrib import admin

from .models import Country, Producter, Car, Comment

admin.site.register(Country)
admin.site.register(Producter)
admin.site.register(Car)
admin.site.register(Comment)