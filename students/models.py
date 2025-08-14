from django.db import models

choice_gender = (
    ('s', 'Please Select Gender'),
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)
# Create your models here.
class Student(models.Model):
    name          = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    father_name   = models.CharField(max_length=100)
    mother_name   = models.CharField(max_length=100)
    birth_place   = models.CharField(max_length=100)
    gender        = models.CharField(choices=choice_gender, default='s')
    
    def __str__(self):
        return self.name
    
class Address(models.Model):
    student           = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='address')
    permanent_address = models.CharField(max_length=150)
    temporary_address = models.CharField(max_length=150)
    
    def __str__(self):
        return self.permanent_address
    
class Education(models.Model):
    student                 = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='education')
    education_qualification = models.CharField(max_length=150)
    started_date            = models.DateField(null=True)
    gradguatee_date         = models.DateField(null=True)
    
    def __str__(self):
        return self.education_qualification