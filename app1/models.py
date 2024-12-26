from django.db import models

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others'),
]
PROVINCE_CHOICES=[
    ('Punjab','Punjab'),
    ('Sindh','Sindh'),
    ('Balochistan','Balochistan'),
    ('Islamabad','Islamabad'),
    ('Khyber Pakhtunkhwa','Khyber Pakhtunkhwa'),
    ('Gilgit-Baltistan','Gilgit-Baltistan'),
    ('Azad Jammu and Kashmir','Azad Jammu and Kashmir'),
    ('Select Province','Select Province')
]


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.PositiveIntegerField()
    date_of_birth = models.DateField(auto_now_add=False,auto_now=False,null=True)
    gender = models.CharField(max_length=25,choices=GENDER_CHOICES, default='others')
    skills = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=200,choices=PROVINCE_CHOICES,default='Select Province')
    city = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='employee_profile_pictures/',null=True, blank=True)
    resume = models.FileField(upload_to='employee_resume/',null=True,blank=True)
    video = models.FileField(upload_to='employee_video/',blank=True,null=True)

    def __str__(self):
        return self.name

# Create your models here.
