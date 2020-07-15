from django import forms
from testapp.models import Student,StudentSignup

class StudentForm(forms.ModelForm):

    class Meta:
        model=Student
        fields='__all__'
        
class StudentSignupForm(forms.ModelForm):
    class Meta:
        model=StudentSignup
        fields='__all__'
