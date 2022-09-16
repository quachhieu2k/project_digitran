from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Employer, Employee, Job, Applyjob
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# employer signup form
class EmployerRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    company = forms.CharField(max_length=30, required=True, help_text='*required')
    address = forms.CharField(max_length=254, help_text='*required')
    website = forms.CharField(max_length=30, required=True, help_text='*required')
    desc = forms.CharField(max_length=1000, required=True, help_text='*required')
    tax_code = forms.CharField(max_length=30, min_length=10,required=True, help_text='*required')
    representative = forms.CharField(max_length=30, required=True, help_text='*required')

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employer = True
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        company = Employer.objects.create(user=user)
        company.company = self.cleaned_data.get('company')
        company.address = self.cleaned_data.get('address')
        company.website = self.cleaned_data.get('website')
        company.desc = self.cleaned_data.get('desc')
        company.tax_code = self.cleaned_data.get('tax_code')
        company.representative = self.cleaned_data.get('representative')
        company.save()
        return user


Gender = (
    ('Nam', "Nam"),
    ('Nữ', "Nữ"),
    ('Khác', "Khác"),
)
class EmployeeRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    gender = forms.ChoiceField(choices = Gender,required=True)
    dob = forms.DateField(required=True, help_text='*required')
    age = forms.IntegerField(required=True)
    home_town = forms.CharField(max_length=254, help_text='*required')
    current_address = forms.CharField(max_length=30, required=True, help_text='*required')

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        student = Employee.objects.create(user=user)
        student.firstname = self.cleaned_data.get('first_name')
        student.lastname = self.cleaned_data.get('last_name')
        student.dob = self.cleaned_data.get('dob')
        student.age = self.cleaned_data.get('age')
        student.home_town = self.cleaned_data.get('home_town')
        student.current_address = self.cleaned_data.get('current_address')
        student.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address_1',
            'address_2',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'check_me_out',
            Submit('submit', 'Sign in')
        )

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('company', 'address', 'website',
                  'desc', 'tax_code', 'representative', 'image' )


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Applyjob
        fields = ['fullname','email','pr', 'cv']




