from django.contrib import admin
from testapp.models import Student,StudentSignup
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['sno','sname','saddr','sschool']

class StudentSignupAdmin(admin.ModelAdmin):
    list_display=['sno','sname','saddr','smobilenumber','semail']


admin.site.register(Student,StudentAdmin)
admin.site.register(StudentSignup,StudentSignupAdmin)
