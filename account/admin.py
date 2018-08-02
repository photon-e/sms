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
			('Permissions', {'fields':('admin','teacher','student', 'groups')}),

	)

	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
	# overrides get_fieldsets to use this attribute when creating a user.

	add_fieldsets = (
		(None, {
			'classes':('wide',),
			'fields':('email','password_1','password_2', 'student', 'teacher', 'groups')
			}

		),
	)
	search_fields = ('email',)
	ordering	  = ('email',)
	filter_horizontal	= ()


admin.site.register(User,UserAdmin)
