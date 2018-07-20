from django.contrib import admin

# # Register your models here.


from .models import (
		CourseOutline,
		Subject,
		Module,
	)



@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display  			= ['title', 'slug']
	prepopulated_fields	 	= {'slug':('title',)}


class ModuleInline(admin.StackedInline):
	model  = Module


@admin.register(CourseOutline)
class CourseOutlineAdmin(admin.ModelAdmin):
	list_display			= ['title', 'subject', 'created']
	list_filter				= ['created', 'subject']
	search_fileds			= ['title', 'overview']
	prepopulated_fields 	= {'slug':('title',)}
	inlines 				= [ModuleInline]