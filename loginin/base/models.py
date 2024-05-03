from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    emp_id=models.CharField(max_length=20,unique=True)
    dob=models.DateField()
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
        ('O','Others'),
    )
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    mobile_no=models.CharField(max_length=15)
    email=models.EmailField()
    designation=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.name