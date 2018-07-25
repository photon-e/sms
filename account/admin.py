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
			('Permissions', {'fields':('admin','teacher','student')}),

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


# @admin.register(UserGroup)
# class GroupAdmin(admin.ModelAdmin):
#     search_fields = ('name',)
#     ordering = ('name',)
#     filter_horizontal = ('permissions',)

#     def formfield_for_manytomany(self, db_field, request=None, **kwargs):
#         if db_field.name == 'permissions':
#             qs = kwargs.get('queryset', db_field.remote_field.model.objects)
#             # Avoid a major performance hit resolving permission names which
#             # triggers a content_type load:
#             kwargs['queryset'] = qs.select_related('content_type')
#         return super().formfield_for_manytomany(db_field, request=request, **kwargs)

admin.site.register(User,UserAdmin)
