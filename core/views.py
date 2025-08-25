from django.shortcuts import render, HttpResponseRedirect
from account.models import CustomUser
from student.models import Student
from teacher.models import Teacher
from parent.models import Parent
from django.contrib import messages
from django.db import transaction


def choose_login_type_page(request):
    return render(request, "core/choose-login-type.html")

def choose_register_type_page(request):
    return render(request, "core/choose-register-type.html")

def register_success(request):
    onboard_type = request.GET.get("onboard")
    return render(request, "core/register/success.html", {"onboard_type":onboard_type})

def student_login(request):
    return render(request, "core/student-login.html")

def parent_login(request):
    return render(request, "core/parent-login.html")

def teacher_login(request):
    return render(request, "core/teacher-login.html")


def student_register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        middle_name = request.POST["middle_name"]
        contact_email = request.POST["contact_email"]
        dob = request.POST["dob"]
        gender = request.POST["gender"]
        password = str(last_name).lower()+"pass"

        # Check if email already exists
        if CustomUser.objects.filter(email=contact_email).exists():
            messages.add_message(request, messages.ERROR, "Email already exists. Please use another one")
            return render(request, "core/register/student-register.html")
        
        try:
            with transaction.atomic():
                new_student = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email=contact_email, login_id=contact_email, middle_name=middle_name, password=password, user_type="STUDENT")
                new_student.save()
                new_student_extra_details = Student.objects.create(gender=gender, dob=dob, account=new_student)
                new_student_extra_details.save()
            return HttpResponseRedirect("/register/success?onboard=student")
        except Exception:
            messages.error(request, "An error occured while creating your account, Please try again!")
            return render(request, "core/register/student-register.html")
    return render(request, "core/register/student-register.html")

def parent_register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        password = request.POST["password"]

        # Check if email already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, "Email already exists. Please use another one")
            return render(request, "core/register/parent-register.html")
        if Parent.objects.filter(phone_number=phone_number).exists():
            messages.add_message(request, messages.ERROR, "Phone number already exists. Please use another one")
            return render(request, "core/register/parent-register.html")
        
        try:
            with transaction.atomic():
                new_user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, login_id=email, password=password, user_type="PARENT")
                new_user.save()
                new_parent_extra_details = Parent.objects.create(phone_number=phone_number, account=new_user)
                new_parent_extra_details.save()
            return HttpResponseRedirect("/register/success?onboard=parent")
        # except IntegrityError:
        #     messages.add_message(request, messages.ERROR, "Either the phone number or email that you provided has already been used.")
        #     return render(request, "core/register/parent-register.html")
        except Exception:
            messages.add_message(request, messages.ERROR, "An error occured while creating your account, Please try again!")
            return render(request, "core/register/parent-register.html")
    return render(request, "core/register/parent-register.html")

def teacher_register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        gender = request.POST["gender"]
        password = request.POST["password"]

        # Check if email already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, "Email already exists. Please use another one")
            return render(request, "core/register/teacher-register.html")
        
        if Teacher.objects.filter(phone_number=phone_number).exists():
            messages.add_message(request, messages.ERROR, "Phone number already exists. Please use another one")
            return render(request, "core/register/teacher-register.html")
        
        try:
            with transaction.atomic():
                new_user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, login_id=email, password=password, user_type="ADMIN")
                new_user.save()
                new_admin_extra_details = Teacher.objects.create(gender=gender, phone_number=phone_number, account=new_user)
                new_admin_extra_details.save()
            return HttpResponseRedirect("/register/success?onboard=admin")
        except Exception:
            messages.add_message(request, messages.ERROR, "An error occured while creating your account, Please try again!")
            return render(request, "core/register/teacher-register.html")
    return render(request, "core/register/teacher-register.html")