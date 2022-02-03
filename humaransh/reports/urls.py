from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    # path('', views.HomeView.as_view(), name="home"),
    path('add_post/',views.AddPostView.as_view(),name="add_post"),
    path('select_doctor/', views.SelectView.as_view(), name='select_doctor'),
    path('choice/', views.choice, name='choice'),
    path('my_feed/',views.FeedView.as_view(),name="my_feed"),
    path('report/<int:pk>', views.ReportDetailView.as_view(), name="report_details"),
    path('patient_history/',views.patientHistoryView.as_view(),name="patient_history"),
    path('patient_history_detail/<int:pk>',views.patientHistoryDetailedView.as_view(),name="patient_history_detail"),
    path('report_doc/<int:pk>', views.patientHistoryDetailView.as_view(), name="report_details_doc"),
    path('ajax/load-patients/', views.load_patients, name='ajax_load_patients')
]