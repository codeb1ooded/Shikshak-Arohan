from django import forms
# Create your forms here.

class resumeForm(forms.Form):
	username = forms.CharField(max_length=200)
	name = forms.CharField(max_length=50)
	age = forms.IntegerField()
	contactNum = forms.CharField(max_length=12)
	email = forms.CharField(max_length=100)
	areaOfExpertise = forms.CharField(max_length=100)
	address = forms.CharField(max_length=200)
	city = forms.CharField(max_length=50)
	state = forms.CharField(max_length=50)
	prefferedLocation = forms.CharField(max_length=50)
	qualification = forms.CharField(max_length=100)
	teachingExperience = forms.IntegerField()
	currentSchool = forms.CharField(max_length=100)
	
	
