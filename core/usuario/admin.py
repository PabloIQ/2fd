from operator import imod
from django.contrib import admin
from .models import Code, CustmUser

# Register your models here.

admin.site.register(Code)
admin.site.register(CustmUser)