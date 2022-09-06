from django.urls import path
from .views import home, login_student, login_company,\
    logout_view, apply_for_job, job_detail
from .import views


urlpatterns = [
    path('',home, name= 'home'),
    path('stu_login',login_student, name= 'login'),
    path('stu_register',views.student_register.as_view(), name='student_register'),
    path('<int:job_id>/apply_for_job/', apply_for_job, name='apply_for_job'),
    path('jobs/<int:job_id>/', job_detail, name='job_detail'),
    # path('jobs/<int:id>', views.JobDetailsView.as_view(), name='jobs-detail'),

    #company
    path('com_login',login_company, name= 'login'),
    path('com_register',views.company_register.as_view(), name='company_register'),
    path('create_job', views.JobCreateView.as_view(), name='create_job'),
    path('list_job', views.JobListView.as_view(), name='list_job'),
    path('job/<int:pk>/', views.JobUpdateView.as_view(), name='update'),
    path('job/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job_delete'),
    path('logout/', logout_view, name= 'logout'),
]