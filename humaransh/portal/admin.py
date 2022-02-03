from django.contrib import admin

# Register your models here.
from .models import Appointment, Contact, User, Patient, Doctor

class Useradmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email','is_patient','is_doctor')

class Patientadmin(admin.ModelAdmin):
    list_display = ('user','pregnancy_month',)
    
class Doctoradmin(admin.ModelAdmin):
    list_display = ('user','specialist','hospital','experience_years')
    
class Contactadmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message')

class Appointmentadmin(admin.ModelAdmin):
    list_display = ('user','patient','doctor','number','date_time','message')
    
admin.site.register(User,Useradmin)
admin.site.register(Patient,Patientadmin)
admin.site.register(Doctor,Doctoradmin)
admin.site.register(Contact,Contactadmin)
admin.site.register(Appointment,Appointmentadmin)