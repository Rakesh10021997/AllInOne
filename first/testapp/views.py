from django.shortcuts import render
from testapp.models import Student,StudentSignup
from testapp import forms
from django.contrib.auth.decorators import login_required
# Create your views here.

#home page
def Home_view(request):
    return render(request,'testapp/base.html')
#login at python exam
@login_required
def javaexam_view(request):
    return render(request,'testapp/java.html')

#login at java
@login_required
def pythonexam_view(request):
    return render(request,'testapp/python.html')

@login_required
def aptitudeexam_view(request):
    return render(request,'testapp/aptitude.html')

#signupform
def StudentSignup_view(request):
    form=forms.StudentSignupForm()
    if request.method=='POST':
        form=forms.StudentSignupForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'testapp/signup.html',{'form':form})




#student details
def Student_details_view(request):
    Student_details=Student.objects.all()
    return render(request,'testapp/student.html',{'Student_details':Student_details})

#directing going to form and insert the data
def Student_form_view(request):
    form=forms.StudentForm
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'testapp/index.html',{'form':form})

#inserting the data in table
def StudentInsert_view(request):
    form=forms.StudentForm
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/home')
    return render(request,'testapp/insert.html',{'form':form})

#delete the data in table
def StudentDelete_view(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return render(request,'testapp/student.html')



#update the data in unsuitable
def StudentUpdate_view(request,id):
    student=Student.objects.get(id=id)

    if request.method=='POST':
        form=forms.StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/home')
    return render(request,'testapp/update.html',{'student':student})
