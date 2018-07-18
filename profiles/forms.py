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
	first_name  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	other_name  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name  	= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	country 	= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	state_of_origin 	= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	residential_area 	= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	mobile_number = models.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-control'}))
	mailing_address  = forms.TextField(widget=forms.Textarea(attrs={'class':'form-control'}))



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
				


# class StudentChangeForm(forms.ModelForm):
# 	class Meta:
# 		model 	= StudentProfile
		

	
	 			
			
		
	