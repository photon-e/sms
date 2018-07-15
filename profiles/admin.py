from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import (
	StudentProfile,
	TeacherProfile,
)
from .forms import (
	StudentCreationForm,
	StudentChangeForm,
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
					'gender',)}),
		('Passport', {'fields':('headshot',)}),
		('Nationality', {'fields':('country', 'state_of_origin', 'zipcode')}),
		('Addresses', {'fields':('residential_area','mailing_address','mobile_number')}),
		('Student Class', {'fields':('student_class',)})

	)

	def full_name(self,obj):
		return ('%s %s' %(obj.first_name, obj.last_name)).upper()
	full_name.short_description = 'Name'

admin.site.register(StudentProfile,StudentAdmin)

