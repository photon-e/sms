from django.contrib.auth.mixins import (
		LoginRequiredMixin,
		PermissionRequiredMixin
)
from django.views.generic.list import ListView
from django.views.generic.edit import(
	CreateView,
	UpdateView,
	DeleteView
)
from django.http import HttpResponse
from django.views import View
from .models import CourseOutline
from django.urls import reverse_lazy

from profiles.models import TeacherProfile

class OwnerMixin(object):
	'''
		Override the get_queryset method
	'''
	def get_queryset(self):
		qs = super(OwnerMixin, self).get_queryset()
		owner = TeacherProfile.objects.get(user = self.request.user)
		return qs.filter(teacher=owner)



class OwnerEditMixin(object):
	'''
		Override the form_valid method
	'''
	def form_valid(self, form):
		form.instance.owner = TeacherProfile.objects.get(user=self.request.user)
		return super(OwnerEditMixin, self).form_valid(form)




class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin):
	model = CourseOutline
	fields = ['subject', 'title', 'slug', 'overview']



class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
	fields = ['subject', 'title', 'slug', 'overview']
	success_url = reverse_lazy('manage_course_list')
	template_name = 'courses/manage/course/form.html'


class ManageCourseListView(OwnerCourseMixin, ListView):
	template_name = 'courses/manage/course/list.html'



class CourseCreateView(PermissionRequiredMixin,OwnerCourseEditMixin, CreateView):
	permission_required = 'courses.add_course'



class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
	permission_required = 'courses.change_course'


class CourseDeleteView(PermissionRequiredMixin,OwnerCourseMixin, DeleteView):
	template_name = 'courses/manage/course/delete.html'
	success_url = reverse_lazy('manage_course_list')
	permission_required = 'courses.delete_course'
