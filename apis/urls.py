from django.urls import path, include
from . import views


urlpatterns = [
    path('students/', views.StudentView.as_view()),
    path('students/<int:pk>/', views.StudentDetailView.as_view()),
    path('address/', views.AddressView.as_view()),
    path('address/<int:pk>/', views.AddressDetailView.as_view()),
    path('education/', views.EducationView.as_view()),
    path('education/<int:pk>/', views.EducationDetailView.as_view()),

]
