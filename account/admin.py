from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import (
	UserChangeForm,
	UserCreationForm,
)
from account.models import (
	User,
)


class UserAdmin(BaseUserAdmin):
	form 			= UserChangeForm
	add_form		= UserCreationForm


	list_display	= ('email',)
	list_filter		= ('admin',)
	fieldsets		= (
			(None,{'fields':('email', 'password')}),
			('Permissions', {'fields':('admin',)}),

	)

	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
	# overrides get_fieldsets to use this attribute when creating a user.

	add_fieldsets = (
		(None, {
			'classes':('wide',),
			'fields':('email','password_1','password_2', 'student', 'teacher')
			}

		),
	)
	search_fields = ('email',)
	ordering	  = ('email',)
	filter_horizontal	= ()


admin.site.register(User,UserAdmin)
# class StudentAdmin(BaseUserAdmin):
# 	form 			= StudentChangeForm
# 	add_form 		= StudentCreationForm

# 	list_display    = ('full_name', 'email', 'student_class')
# 	list_filter     = ('student_class',)
# 	fieldsets  		= (
# 			(None, {'fields':('first_name', 'other_name', 'last_name', 'email')}),
# 			('Personal info', {'fields':('first_name', 
# 										 'date_of_birth',
# 										 'nationality', 
# 										 'state_of_origin',
# 										 'residential_area',
# 										 'mailing_address',)}),
# 			('Student Class', {'fields':('student_class',)}),
# 			('Permissions', {'fields':('is_student',)}),
# 	)
# 	add_fieldsets = (
# 		(None, {
# 			'classes':('wide',),
# 			'fields':('email', 'date_of_birth')
# 			}

# 		),
# 	)
# 	search_fields = ('first_name', 'other_name','last_name',  'email')
# 	ordering	 = ('student_class',)
# 	filter_horizontal = ()


# class TeacherAdmin(BaseUserAdmin):
# 	form 			= TeacherChangeForm
# 	add_form 		= TeacherCreationForm

# 	list_display    = ('full_name', 'email',)
# 	list_filter 	= ('is_teacher',)
# 	fieldsets  		= (
# 			(None, {'fields':('first_name', 'other_name', 'last_name', 'email')}),
# 			('Personal info', {'fields':(
# 										 'date_of_birth',
# 										 'mobile_number',
# 										 'nationality', 
# 										 'state_of_origin',
# 										 'residential_area',
# 										 'mailing_address',)}),
# 			('Qualifications', {'fields':('qualifications',)}),
# 			('Permissions', {'fields':('is_teacher',)}),
# 	)
# 	add_fieldsets = (
# 		(None, {
# 			'classes':('wide',),
# 			'fields':(
# 				'first_name', 
# 				'other_name', 
# 				'last_name',
# 				'email',
# 				'password_1', 
# 				'headshot',
# 				'gender',
# 				'nationality',
# 				'state_of_origin',
# 				'residential_area',
# 				'mailing_address',
# 				'mobile_number',
# 				'is_teacher',
# 				'qualifications',)
# 			}

# 		),
# 	)
# 	search_fields = ('first_name', 'other_name','last_name',  'email')
# 	ordering 	  = ('date_of_joining',)
# 	filter_horizontal = ()





# admin.site.register(MyUser, UserAdmin)
# admin.site.register(Student, StudentAdmin)
# admin.site.register(Teacher, TeacherAdmin)
# admin.site.unregister = Group