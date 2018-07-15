from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from .models import (

	StudentProfile,
	TeacherProfile
)




class StudentCreationForm(forms.ModelForm):
	password_1	= forms.CharField(label='Password', widget=forms.PasswordInput)
	password_2	= forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

	class Meta:
		model = StudentProfile
		fields = (
			'first_name',
			'other_name',
			'last_name',
			'headshot',
			'gender',
			'country',
			'state_of_origin',
			'residential_area',	
			'mailing_address',	
			'mobile_number',
			)

	def clean_password_2(self):
		password_1 	= self.cleaned_data.get('password_1')
		password_2  = self.cleaned_data.get('password_2')
		if password_1 and password_2 and password_1 != password_2:
			raise forms.ValidationError('Password didn\'t match')
		return password_2

	def save(self, commit=False):
		user = super(StudentCreationForm,self).save(commit=True)
		user.set_password(self.cleaned_data['password_1'])
		if commit:
			user.save()
		return user
				


class StudentChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model 	= StudentProfile
		fields 	= ('first_name', 'last_name')

	def clean_password(self):
		return self.initial['password']

	 			
			
		
	