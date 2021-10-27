from django.contrib import admin

# Register your models here.

from . models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Login)
admin.site.register(User)
admin.site.register(UserContact)
admin.site.register(CustomerContact)
