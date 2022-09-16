from django.urls import path
from .views import home, login_student, \
    logout_view, apply_for_job, job_detail, register
from .import views


urlpatterns = [
    path('',home, name= 'home'),
    path('register',register, name= 'register'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('accounts/login/',login_student, name= 'login'),
    path('logout/', logout_view, name= 'logout'),
    path('stu_register',views.student_register.as_view(), name='student_register'),
    path('<int:job_id>/apply_job/', apply_for_job, name='apply_for_job'),
    path('jobs/<int:job_id>/', job_detail, name='job_detail'),
    path('list_apply', views.ApplyListView.as_view(), name='list_apply'),

    #company
    path('com_register',views.company_register.as_view(), name='company_register'),
    path('profile', views.UpdateProfile.as_view(), name='profile'),
    path('create_job', views.JobCreateView.as_view(), name='create_job'),
    path('list_job', views.JobListView.as_view(), name='list_job'),
    path('job/<int:pk>/', views.JobUpdateView.as_view(), name='update'),
    path('job/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job_delete'),
    path('job/<int:pk>/view', views.StudentListView.as_view(), name='view_stu'),
    #path('student_detail/<int:pk>', views.StudentDetailView.as_view(), name='student_detail'),
]