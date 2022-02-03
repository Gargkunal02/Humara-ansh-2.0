from django.db import models

# Create your models here.

from django.contrib.auth.models import User
# from django.reports.views import choice
from portal.models import Doctor, Patient
from django.urls import reverse
from django.db.models import CheckConstraint, Q, F

def validate_patient(patient):
	if (Post.patient.choice==Post.doctor.user.id):
		return patient
	else: 
		print("error")

class Post(models.Model):
	title = models.CharField(max_length=255)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reciever', default=None)
	body = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True, editable=False)
	file = models.FileField()
	
	# class Meta:
	# 	constraints = [models.CheckConstraint(
    #             name="%(app_label)s_%(class)s_mapped_patients",
    #             check=models.Q(Patient.objects.filter(choice=37)),
    #         )
    #     ]		

	def get_absolute_url(self):
		return reverse("portal:doctor_home")
	
	def mapping(self):
		if self.patient.choice == self.doctor.user.id:
			return self

class Prescriptions(models.Model):
	title = models.CharField(max_length=255)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reciever_pres', default=None)
	body = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True, editable=False)