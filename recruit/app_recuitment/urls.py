from django.urls import path
from .views import home, login_student, login_company, logout_view
from .import views
urlpatterns = [
    path('',home, name= 'home'),
    path('stu_login',login_student, name= 'login'),
    path('com_login',login_company, name= 'login'),
    path('com_register/',views.company_register.as_view(), name='company_register'),
    path('stu_register/',views.student_register.as_view(), name='student_register'),

]