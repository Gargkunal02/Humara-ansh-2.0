from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, edit
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import Post
from portal.models import Doctor, Patient

class SelectView(ListView):
	model = Doctor
	template_name = 'reports/selected.html'

# class FeedView(ListView):
# 	# model = Doctor
# 	template_name = '.html'

class AddPostView(CreateView):
	model = Post
	# form_class = PostForm
	template_name = 'reports/add_report.html'

	# class Meta:
	# 	Post.parent.choice = Post.doctor.user.id

def load_patients(request):
	doctor_id = request.GET.get('doctor')
	patients = Patient.objects.filter(choice = doctor_id)
	return render(request, 'reports/patient_dropdown_list_options.html', {'patients':patients})

def choice(request):
	Patient.objects.filter(user__username=request.user).update(choice = request.POST['doc'])
	return HttpResponseRedirect(reverse('portal:patient_home'))

class ReportDetailView(DetailView):
	model = Post
	template_name = 'reports/report_details.html'
	context_object_name = 'post'

	def get_context_data(self, *args, **kwargs):
		context = super(ReportDetailView, self).get_context_data(**kwargs)
		context[self.context_object_name] = get_object_or_404(Post, id=self.kwargs['pk'])
		# context[self.context_object_name] = self.object
		return context

class FeedView(ListView):
	model = Post
	template_name = 'reports/my_feed.html'
	ordering = ['-post_date']

class patientHistoryView(ListView):
	model = Patient
	template_name = 'reports/patient_history.html'

class patientHistoryDetailedView(ListView):
	model = Post
	template_name = 'reports/patient_history_detail.html'
	ordering = ['-post_date']

	def get_context_data(self, *args, **kwargs):
		context = super(patientHistoryDetailedView, self).get_context_data(**kwargs)
		patient = get_object_or_404(Patient, user_id=self.kwargs['pk'])
		context["patient"] = patient.user
		context["patientid"] = patient.user.id
		return context

class patientHistoryDetailView(DetailView):
	model = Post
	template_name = 'reports/report_details_doc.html'
	ordering = ['-post_date']

	def get_context_data(self, *args, **kwargs):
		context = super(patientHistoryDetailView, self).get_context_data(**kwargs)
		context[self.context_object_name] = get_object_or_404(Post, id=self.kwargs['pk'])
		# context[self.context_object_name] = self.object
		return context

