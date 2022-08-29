from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from .form import EmployerRegisterForm, EmployeeRegisterForm
from .models import Employer, User
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.


def home(request, *args, **kwargs):
    return render(request, 'student/stu_home.html')


class company_register(CreateView):
    model = User
    form_class = EmployerRegisterForm
    template_name = 'company/com_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class student_register(CreateView):
    model = User
    form_class = EmployeeRegisterForm
    template_name = 'student/stu_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_student(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'student/stu_login.html',
    context={'form':AuthenticationForm()})

def login_company(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'company/com_login.html',
    context={'form':AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')

# def company_register(request, *args, **kwargs):
#     form = EmployerRegisterForm(request.POST)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         raw_password = form.cleaned_data.get('password1')
#         com = Employer()
#         com.username = request.POST.get('username')
#         com.company = request.POST.get('company_name')
#         com.address = request.POST.get('address')
#         com.website = request.POST.get('website')
#         com.desc = request.POST.get('desc')
#         com.tax_code = request.POST.get('tax_code')
#         com.representative = request.POST.get('representative')
#         com.save()
#         user = authenticate(username=username, password= raw_password)
#         login(request, user)
#         return redirect('company/com_home')
#     else:
#         return render(request, 'company/com_register.html', {'form': form})
#
# def student_register(request, *args, **kwargs):
#     form = EmployeeSignUpForm(request.POST)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         raw_password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password= raw_password)
#         login(request, user)
#         return redirect('student/stu_home')
#     else:
#         return render(request, 'student/stu_register.html', {'form': form})
