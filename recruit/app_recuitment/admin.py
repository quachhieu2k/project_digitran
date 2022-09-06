from django.contrib import admin
from .models import User, Employer, Employee, Job, Applyjob
# Register your models here.
admin.site.register(User),
admin.site.register(Employer),
admin.site.register(Employee),
admin.site.register(Job),
admin.site.register(Applyjob)
