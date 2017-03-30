from api.models import Teacher
from django import forms

class PostForm(forms.ModelForm):
	class Meta:
		model = Teacher
		exclude=['username','password',]