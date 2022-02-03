from unicodedata import name
from django.shortcuts import render

# Create your views here.
from portal.models import User, Patient,  Doctor
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from reports.views import *

from .models import Appointment, Contact, Patient
from .decorators import patient_required

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_doctor:
                # messages.info(request, f"You are now logged in as {username}")
                return redirect('portal:doctor_home')
            else:
                return redirect('portal:patient_home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request = request,
                    template_name = "registration/login.html",)

class SignUpView(TemplateView):
    template_name = 'portal/index-home.html'

class ContactUsView(TemplateView):
    template_name = 'portal/contact.html'

class TeamView(TemplateView):
    template_name = 'portal/team.html'

class FeedView(TemplateView):
	# model = Doctor
	template_name = 'portal/blog.html'

def PatientSignUpView(request):
    if request.method == 'POST':
        username = request.POST['company']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Month_of_Pregnancy = request.POST['Month_of_Pregnancy']
        password1 = request.POST['password']
        password2 = request.POST['cpassword']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'portal/index.html', {'message': 'Email already registered.'})
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
            user.is_patient = True
            user.save()
            patient = Patient(user=user)
            patient.pregnancy_month = Month_of_Pregnancy
            patient.save()
            return redirect('portal:patient_home')
            # return render(request, 'portal/patient_home.html')
    return render(request, 'portal/index.html')

def DoctorSignUpView(request):
    if request.method == 'POST':
        username = request.POST['company']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Specialist = request.POST['Specialist']
        experience_years = request.POST['experience_years']
        hospital = request.POST['hospital']
        password1 = request.POST['password']
        password2 = request.POST['cpassword']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'portal/doc_signup.html', {'message': 'Email already registered.'})
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
            user.is_doctor = True
            user.save()
            doctor = Doctor(user=user)
            doctor.specialist = Specialist
            doctor.experience_years = experience_years
            doctor.hospital = hospital
            doctor.save()
            return redirect('portal:doctor_home')
    return render(request, 'portal/doc_signup.html')

def PatientHomeView(request):
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    context={
        'doctor':doctor,
        'patient':patient,
    }
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        print(contact)
        return render(request, 'portal/patient_home.html',context)
    return render(request, 'portal/patient_home.html',context)

# class PatientHomeView(ListView):
#     model = Patient
#     template_name = 'portal/patient_home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['patient'] = Patient.objects.all()  # or whatever
#         context['doctor'] = Doctor.objects.all()  # or whatever
#         return context

# class DoctorHomeView(ListView):
#     model = Doctor
#     template_name = 'portal/doctor_home.html'
    
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     subject = request.POST['subject']
    #     message = request.POST['message']
    #     contact = Contact(name=name,email=email,subject=subject,message=message)
    #     contact.save()
    #     print(contact)
    #     return render(request, 'portal/contact.html')

def DoctorHomeView(request):
    doctor = Doctor.objects.all()
    x={
        'doctor':doctor,
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        print(contact)
        return render(request, 'portal/doctor_home.html',x)
    return render(request, 'portal/doctor_home.html',x)

@login_required
def login_success(request):
    if request.user.is_doctor:
        return HttpResponseRedirect(reverse('portal:doctor_home'))
    else:
        return HttpResponseRedirect(reverse('portal:patient_home'))

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        print(contact)
        return render(request, 'portal/contact.html')
    return render(request, 'portal/contact.html')

def App(request):
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()
    context={
        'doctor':doctor,
        'patient':patient,
        'appointment':appointment,
    }
    return render(request,'portal/Appointment.html',context)