from django.contrib import admin
from .models import Student, Address, Education
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_birth', 'gender']
    
class AddressAdmin(admin.ModelAdmin):
    list_display = ['student', 'permanent_address', 'temporary_address']
    
class EducationAdmin(admin.ModelAdmin):
    list_display = ['student', 'education_qualification', 'started_date', 'gradguatee_date']
    
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Education, EducationAdmin)

