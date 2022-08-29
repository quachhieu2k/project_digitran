from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):

    username = models.CharField(max_length=200, unique=True, blank=False)
    email = models.EmailField(max_length=200, unique=True, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    is_employer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Employer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )

    company = models.CharField(max_length=200, default=None, blank=True, null=True)
    address = models.CharField(max_length=100, default=None, blank=True, null=True)
    website = models.CharField(max_length=255, default=None, blank=True, null=True)
    desc = models.CharField(max_length=1000, default=None, blank=True, null=True)
    tax_code = models.CharField(max_length=11, default=None, blank=True, null=True)
    representative = models.CharField(max_length=45, default=None, blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.company


class Employee(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True)

    firstname = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    home_town = models.CharField(max_length=100, blank=True, null=True)
    current_address = models.CharField(max_length=100, blank=True, null=True)
    # college = models.CharField(max_length=45, blank=True, null=True)
    # major = models.CharField(max_length=45, blank=True, null=True)
    # start_year = models.DateField(blank=True, null=True)
    # grad_year = models.DateField(blank=True, null=True)
    # gpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return self.firstname + self.lastname

class Education(models.Model):
    student = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    college = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    major = models.CharField(max_length=45, blank=True, null=True)
    start_year = models.DateField(blank=True, null=True)
    grad_year = models.DateField(blank=True, null=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)


JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)
class Job(models.Model):
    company = models.ForeignKey(Employer, models.DO_NOTHING)
    title = models.CharField(max_length=45, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    requirements = models.TextField(blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    number_req = models.IntegerField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.company + 'vs' + self.title


class Applyjob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    created_at = models.DateTimeField(default=timezone.now)
