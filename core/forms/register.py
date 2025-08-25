from django.forms import ModelForm, CharField
from account.models import CustomUser
from student.models import Student
from teacher.models import Teacher
from parent.models import Parent

class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "middle_name", "email"]
    

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["gender", "dob"]

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ["gender", "dob"]

class ParentForm(ModelForm):
    class Meta:
        model = Parent
        fields = ["phone_number"]