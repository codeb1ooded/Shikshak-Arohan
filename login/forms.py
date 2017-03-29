#login/forms.py
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from login.models import *

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class schoolAdd(forms.Form):
	#user = forms.CharField(max_length=50)
	pass1=forms.CharField(max_length=100)
	#user = forms.CharField(label="Username", max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    #pass1 = forms.CharField(label="Password", max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

	name=forms.CharField(max_length=100)
	state=forms.ModelMultipleChoiceField(queryset=State.objects.all())
	timing=forms.CharField(max_length=100)
	address=forms.CharField(max_length=100)
	district=forms.ModelMultipleChoiceField(queryset=District.objects.all())
	city=forms.ModelMultipleChoiceField(queryset=City.objects.all())
	numOfStudents=forms.IntegerField()
	numOfTeachers=forms.IntegerField()
	latitude=forms.FloatField()
	longitude=forms.FloatField()
	wifi_zone=forms.BooleanField()