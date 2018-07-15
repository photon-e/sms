from django import forms
from account.models import (
	User,
)
from django.contrib.auth.forms import ReadOnlyPasswordHashField


## User Creation Form
class UserCreationForm(forms.ModelForm):
	"""
		A form for creating new users. INcludes all the required field,
		 plus a repeated password field.
	"""
	password_1	= forms.CharField(label='Password', widget=forms.PasswordInput)
	password_2	= forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

	class Meta:
		model 	= User
		fields	= ('email','admin', 'active')

	def clean_password_2(self):
		# check the two password entries match
		password_1	= self.cleaned_data.get('password_1') 
		password_2 	= self.cleaned_data.get('password_2')
		if password_1 and password_2 and password_1 != password_2:
			raise forms.ValidationError('Password donn\'t match ')
		return password_2

	def save(self, commit=True):
		''' overiding the save method '''
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password_1'])
		if commit:
			user.save()
		return user


# User Change Form
class UserChangeForm(forms.ModelForm):
	"""A form for updating users. Includes all the fields on
	the user, but replaces the password field with admin's
	password hash display field.
	"""

	password = ReadOnlyPasswordHashField()

	class Meta:
		model 	= User
		fields	= ('email', 'password','active', 'admin')

	def clean_password(self):
		# Regardless of what the user provides, return the initial value.
		# This is done here, rather than on the field, because the
		# field does not have access to the initial value
		return self.initial['password']

# class StudentCreationForm(forms.ModelForm):
# 	password_1  = forms.CharField(label='Password', widget=forms.PasswordInput)
# 	password_2 	= forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
	
# 	class Meta:
# 		model 	= Student
# 		fields	= (
# 				'first_name', 
# 				'other_name', 
# 				'last_name', 
# 				'email',
# 				'headshot',
# 				'gender',
# 				'nationality',
# 				'state_of_origin',
# 				'residential_area',
# 				'mailing_address',
# 				'mobile_number',
# 				'is_student',
# 				'student_class',
# 				)	

# 	def clean_password_2(self):
# 		password_1 = self.cleaned_data.get('password_1')
# 		password_2 = self.cleaned_data.get('password_2')
# 		if password_1 and password_2 and password_1 != password_2:
# 			raise forms.ValidationError('Password don\'t match')
# 		return self.password_2

# 	def save(self, commit=True):
# 		user = super().save(commit=False)
# 		user.set_password(self.cleaned_data['password_1'])
# 		if commit:
# 			user.save()
# 		return user


# class StudentChangeForm(forms.ModelForm):
# 	"""A form for updating students. Includes all the fields on
# 	the user, but replaces the password field with admin's
# 	password hash display field.
# 	"""

# 	password = ReadOnlyPasswordHashField()

# 	class Meta:
# 		model 	= Student
# 		fields	= (
# 					'first_name', 
# 					'other_name', 
# 					'last_name',
# 					'email',
# 					'password', 
# 					'headshot',
# 					'gender',
# 					'nationality',
# 					'state_of_origin',
# 					'residential_area',
# 					'mailing_address',
# 					'mobile_number',
# 					'is_student',
# 					'student_class',
# 						)	
# 	def clean_password(self):
# 		# Regardless of what the user provides, return the initial value.
# 		# This is done here, rather than on the field, because the
# 		# field does not have access to the initial value
# 		return self.initial['password']


# class TeacherCreationForm(forms.ModelForm):
# 	password_1 	= forms.CharField(label='Password', widget=forms.PasswordInput)
# 	password_2 	= forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

# 	class Meta:
# 		model 	= Teacher
# 		fields	= (
# 					'first_name', 
# 					'other_name', 
# 					'last_name',
# 					'email', 
# 					'headshot',
# 					'gender',
# 					'nationality',
# 					'state_of_origin',
# 					'residential_area',
# 					'mailing_address',
# 					'mobile_number',
# 					'is_teacher',
# 					'qualifications'
# 		)

# 	def cleaned_password_2(self):
# 		password_1  	= self.cleaned_data.get('password_1')
# 		password_2 		= self.cleaned_data.get('password_2')

# 		if password_1 and passwprd_2 and password_1 != password_2:
# 			raise forms.ValidationError('Passoword don\'t match')
# 		return password_2

# 	# def save(self, commit=True):
# 	# 	user = super().save(commit=False)
# 	# 	user.set_password(self.cleaned_data['password_1'])
# 	# 	if commit:
# 	# 		user.save()
# 	# 	return user

# class TeacherChangeForm(forms.ModelForm):
# 	"""A form for updating teachers. Includes all the fields on
# 	the user, but replaces the password field with admin's
# 	password hash display field.
# 	"""

# 	password = ReadOnlyPasswordHashField()

# 	class Meta:
# 		model 	= Teacher
# 		fields	= (
# 					'first_name', 
# 					'other_name', 
# 					'last_name',
# 					'email',
# 					'password', 
# 					'headshot',
# 					'gender',
# 					'nationality',
# 					'state_of_origin',
# 					'residential_area',
# 					'mailing_address',
# 					'mobile_number',
# 					'is_student',
# 					'qualifications'
					
# 						)	
# 	def clean_password(self):
# 		# Regardless of what the user provides, return the initial value.
# 		# This is done here, rather than on the field, because the
# 		# field does not have access to the initial value
# 		return self.initial['password']
