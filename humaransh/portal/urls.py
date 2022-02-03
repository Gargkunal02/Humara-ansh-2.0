from django.urls import include, path
from .views import App, Appointment, ContactUsView, FeedView, PatientSignUpView, DoctorSignUpView, PatientHomeView, DoctorHomeView, TeamView, contact_view, login_success, login_request

app_name = 'portal'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('patient_sign_up/', PatientSignUpView, name='patient_signup'),
    path('doctor_sign_up/', DoctorSignUpView, name='doctor_signup'),
    path('doctor_home/', DoctorHomeView, name='doctor_home'),
    path('patient_home/', PatientHomeView, name='patient_home'),
    path('login_success/', login_success, name='login_success'),
    path('login/', login_request, name="login"),
    path('contact_us/', contact_view, name='Contact_Us'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('team/', TeamView.as_view(), name='team'),
    path('appointment/',App,name='appointment')
]