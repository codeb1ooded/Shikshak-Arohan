#login/forms.py
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from login.models import State

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class schoolAdd(forms.Form):
	user = forms.CharField(max_length=50)
	name=forms.CharField(max_length=100)
	state=forms.ModelMultipleChoiceField(queryset=State.objects.all())