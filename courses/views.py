from django.views.generic.list import ListView
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



class OwnerMixin(object):
	'''
		Override the get_queryset method
	'''
	def get_queryset(self):
		qs = super(OwnerMixin, self).get_queryset()
		return qs.filter(owner=self.request.user)

class OwnerEditMixin(object):
	'''
		Override the form_valid method
	'''
	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(OwnerEditMixin, self).form_valid(form)


class OwnerCourseMixin(OwnerMixin):
	model = CourseOutline


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
	fields = ['subject', 'title', 'slug', 'overview']
	success_url = reverse_lazy('manage_course_list')
"""

class BaseClass(View):
	greetings = "Good Moring"

	def get(self,request):
		return HttpResponse(str(self.greetings))

class ChildClass(View):
	greetings = "Good Afternoon"

	def get(self, request):
		return HttpResponse(self.greetings)


"""