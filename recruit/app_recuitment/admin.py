from django.contrib import admin
from .models import User, Employer, Employee
# Register your models here.
admin.site.register(User),
admin.site.register(Employer),
admin.site.register(Employee),
# admin.site.register(College),
# admin.site.register(Education)
