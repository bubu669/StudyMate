from django.urls import path
from signup import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.signup_view, name='signup'),
    path('signup/',views.signup_view,name="sign_up"),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    
    
]

