from django.contrib import admin

from users.models import Booking, Contact
from users.models import User
# Register your models here.
admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(User)