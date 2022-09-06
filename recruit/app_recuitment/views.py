from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login,authenticate,logout
from .form import EmployerRegisterForm, EmployeeRegisterForm, ApplicationForm, CompanyProfileForm
from .models import Employer, User, Job
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorator import company_required, student_required
# Create your views here.

#TRANG HOME
def home(request):
    jobs = Job.objects.all()
    company = Employer.objects.all()
    if request.user.is_authenticated:
        if request.user.is_employer:
            return render(request, 'company/com_home.html')
        else:
            return render(request, 'student/stu_home.html', {'jobs': jobs, 'company': company})
    return render(request, 'student/stu_home.html', {'jobs': jobs, 'company': company})


def register(request):
    return render(request, 'student/register_form.html')


def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    company = Employer.objects.get(user = job.company)
    return render(request, 'student/job_detail.html', {'job': job, 'company': company})


# class JobDetailsView(DetailView):
#     model = Job
#     template_name = 'student/job_detail.html'
#     context_object_name = 'job'
#     pk_url_kwarg = 'id'

    # def get_object(self, queryset=None):
    #     obj = super(JobDetailsView, self).get_object(queryset=queryset)
    #     if obj is None:
    #         raise Http404("Job doesn't exists")
    #     return obj
    #
    # def get(self, request, *args, **kwargs):
    #     try:
    #         self.object = self.get_object()
    #     except Http404:
    #         # redirect here
    #         raise Http404("Job doesn't exists")
    #     context = self.get_context_data(object=self.object)
    #     return self.render_to_response(context)

# ACCOUNT VIEW

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



class company_register(CreateView):
    model = User
    form_class = EmployerRegisterForm
    template_name = 'company/com_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

# def login_company(request):
#     if request.method=='POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None :
#                 login(request,user)
#                 return redirect('/')
#             else:
#                 messages.error(request,"Invalid username or password")
#         else:
#                 messages.error(request,"Invalid username or password")
#     return render(request, 'company/com_login.html',
#     context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

#COMPANY VIEW
@method_decorator([login_required, company_required], name='dispatch')
class UpdateProfile(UpdateView):
    model = Employer
    form_class = CompanyProfileForm
    template_name = 'company/update_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user.employer

    def form_valid(self, form):
        messages.success(self.request, 'Interests updated with success!')
        return super().form_valid(form)


@method_decorator([login_required, company_required], name='dispatch')
class JobCreateView(CreateView):
    model = Job
    fields = ('title', 'desc', 'type', 'requirements', 'benefits', 'number_req', 'deadline'  )
    template_name = 'company/create_job.html'

    def form_valid(self, form):
        job = form.save(commit=False)
        job.company = self.request.user
        job.save()
        # messages.success(self.request, 'tạo job thành công.')
        return redirect('/list_job', job.pk)

@method_decorator([login_required, company_required], name='dispatch')
class JobListView(ListView):
    model = Job
    # ordering = ('title',)
    context_object_name = 'jobbs'
    template_name = 'company/list_jobs.html'

    def get_queryset(self):
        queryset = self.request.user.jobbs \
            .select_related('company')
        return queryset


@method_decorator([login_required, company_required], name='dispatch')
class JobUpdateView(UpdateView):
    model = Job
    fields = ('title', 'desc', 'type', 'requirements', 'benefits', 'number_req', 'deadline')
    context_object_name = 'jobs'
    template_name = 'company/update_job.html'

    def get_success_url(self):
        return reverse('update', kwargs={'pk': self.object.pk})


@method_decorator([login_required, company_required], name='dispatch')
class JobDeleteView(DeleteView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'company/delete_job.html'
    success_url = reverse_lazy('list_job')

    def delete(self, request, *args, **kwargs):
        jobs = self.get_object()
        return super().delete(request, *args, **kwargs)


#STUDENT VIEW

@login_required
@student_required
def apply_for_job(request, job_id):
    job = Job.objects.get(pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.save()

            return redirect('/')
    else:
        form = ApplicationForm()

    return render(request, 'student/apply_job.html', {'form': form, 'job': job})

