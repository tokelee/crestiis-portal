from django.urls import path
from . import views

urlpatterns = [
    path("login", views.choose_login_type_page, name="choose-login-type-page"),
    path("register", views.choose_register_type_page, name="choose-register-type"),
    path("forgot-password", views.forgot_password, name="forgot-password"),
   
    path("login/student", views.student_login, name="student-login"),
    path("login/parent", views.parent_login, name="parent-login"),
    path("login/teacher", views.teacher_login, name="teacher-login"),
    
    path("register/student", views.student_register, name="student-register"),
    path("register/parent", views.parent_register, name="parent-register"),
    path("register/teacher", views.teacher_register, name="teacher-register"),
    path("register/success", views.register_success, name="register-success"),
    # path("login/teacher", views.choose_login_type_page, name="choose-login-type-page"),
]