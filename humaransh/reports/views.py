from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, edit, TemplateView
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


# class AddPostView(ListView):
# 	model = Patient
# 	template_name = 'reports/patient_dropdown_list_options.html'
# 	context_object_name = 'patient'

# 	def get_context_data(self, *args, **kwargs):
# 		context = super(AddPostView, self).get_context_data(**kwargs)
# 		context[self.context_object_name] = get_object_or_404(Patient.objects.all())
# 		return context

# 	class Meta:
# 		Post.parent.choice = Post.doctor.user.id

def post_view(request):
	patient = Patient.objects.all()
	context={
        'patient':patient,
    }

	if request.method == 'POST':
		title = request.POST['title']
		doctor = request.POST['doctor']
		doctor = Doctor.objects.get(pk=doctor)
		patient = request.POST['patient']
		patient = Patient.objects.get(pk=patient)
		body = request.POST['body']
		file = request.FILES.get('file', False)
		post = Post(title=title,doctor=doctor,patient=patient,body=body,file=file)
		post.save()
		print(post)
		return render(request, 'reports/add_report.html', context)
	return render(request, 'reports/add_report.html', context)

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

