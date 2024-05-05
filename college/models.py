from django.db import models

# Create your models here.
class Student(models.Model):
    email = models.EmailField(max_length=30,null=True)
    password = models.CharField(max_length=30)

    class Meta():
        db_table = 'student'

class StudentData(models.Model):
    fname = models.CharField(max_length=30,null=False)
    sname = models.CharField(max_length=30,null=False)
    lname = models.CharField(max_length=30,null=False)
    gender = models.CharField(max_length=10,null=False)
    dob = models.DateField(null=False)
    email2 = models.EmailField(null=False,blank=True)
    community = models.CharField(max_length=20,null=False)
    nationality = models.CharField(max_length=20,null=False)
    phone = models.IntegerField(default="")
    address = models.CharField(max_length=20,null=False)
    city = models.CharField(max_length=20,null=False)
    district = models.CharField(max_length=20,null=False)
    state = models.CharField(max_length=40,null=False)
    pincode = models.IntegerField(default="")
    rollno10 = models.CharField(max_length=20,null=False)
    year10 = models.IntegerField(default="")
    board10 = models.CharField(max_length=40,null=False)
    rollno12 = models.CharField(max_length=20,null=False)
    year12 = models.IntegerField(default="")
    board12 = models.CharField(max_length=40,null=False)
    photo = models.FileField(upload_to='upload/',null=False)
    sign = models.FileField(upload_to='upload/',null=False)

