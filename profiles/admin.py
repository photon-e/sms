from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import (
	StudentProfile,
	TeacherProfile,
	SubjectProfile,
)


# Register your models here.


class StudentAdmin(admin.ModelAdmin):
	list_display 	= ('full_name','student_class',)
	list_filter 	= ('student_class',)
	ordering		= ('student_class',)
	fieldsets 		= (
		(None, {
			'fields':('user',)
		}),
		('Personal Info', {
					'fields':('first_name', 
					'last_name',
					'other_name',
					'gender',
					'date_of_birth',
					)}),
		('Credentials', {'fields':('photo','qualification')}),
		('Nationality', {'fields':('country', 'state_of_origin', 'zipcode')}),
		('Addresses', {'fields':('residential_area','mailing_address','mobile_number')}),
		('Student Class', {'fields':('student_class',)}),
		('Student Subject', {'fields':('subjects','date_of_joining')})

	)

	def full_name(self,obj):
		return ('%s %s %s' %(obj.first_name, obj.other_name ,obj.last_name)).upper()
	full_name.short_description = 'Name'

class TeacherAdmin(admin.ModelAdmin):
	list_display 	= ('teacher_full_name','teacher_class')
	list_filter		= ('teacher_class',)
	ordering 		= ('teacher_class',)
	search_fields 	= ('first_name','last_name','teacher_class')
	fieldsets 		= (
	(None, {
			'fields':('user',)
		}),
		('Personal Info', {
					'fields':('first_name', 
					'last_name',
					'other_name',
					'gender',
					'date_of_birth',)}),
		('Credentials', {'fields':('photo','qualification')}),
		('Nationality', {'fields':('country', 'state_of_origin', 'zipcode')}),
		('Addresses', {'fields':('residential_area','mailing_address','mobile_number')}),
		('Teacher Class', {'fields':('teacher_class',)}),
		('Teacher Subject', {'fields':('subjects','date_of_joining')})
	)
	def teacher_full_name(self, obj):
		return ('%s %s %s' %(obj.first_name, obj.other_name ,obj.last_name)).upper()
	teacher_full_name.short_description = 'Teacher_Name'

	# def full_name(self, obj):
	# 	return ('%s %s'%(obj.first_name. obj.last_name)).upper()
	# full_name.short_description = 'TName'
	

class SubjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields 	= {'slug':('title',)}

admin.site.register(StudentProfile,StudentAdmin)
admin.site.register(TeacherProfile, TeacherAdmin)
admin.site.register(SubjectProfile,SubjectAdmin)
