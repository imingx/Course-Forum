from django.urls import path
from . import views

urlpatterns = [
    path('StudentLogin/', views.StudentLogin.as_view()),
    path('StudentRegister/', views.StudentRegister.as_view()),
    path('TeacherLogin/', views.StudentLogin.as_view())
]