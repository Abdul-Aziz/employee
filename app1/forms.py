from django import forms
from .models import Employee

SKILL_CHOICES = [
    ('Python', 'Python'),
    ('Django', 'Django'),
    ('Flask', 'Flask'),
    ('React', 'React'),
    ('Vue', 'Vue'),
    ('Angular', 'Angular'),
    ('SQL', 'SQL'),
    ('NoSQL', 'NoSQL')
]

class EmployeeForm(forms.ModelForm):
    skills = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=SKILL_CHOICES)
    class Meta:
        model = Employee
        fields = "__all__"
        labels = [
            ('name', 'Full Name'),
            ('email', 'Email Address'),
            ('mobile', 'Mobile Number'),
            ('date_of_birth', 'Date of Birth'),
            ('gender', 'Gender'),
            ('skills', 'Skills'),
            ('state', 'State'),
            ('city', 'City'),
            ('profile_picture', 'Profile Picture'),
            ('resume', 'Resume'),
            ('video', 'Video')
        ]
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'date_of_birth':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'skills':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'profile_picture':forms.FileInput(attrs={'class':'form-control-file'}),
            'resume':forms.FileInput(attrs={'class':'form-control-file'}),
            'video':forms.FileInput(attrs={'class':'form-control-file'}),
        }
