from django.views.generic.list import ListView
from django.http import HttpResponse
from django.views import View
from .models import CourseOutline


# class ManageCourseListView(ListView):
# 	model = Course
# 	template_name = 'courses/manage/course/list.html'


# 	def get_queryset(self):
# 		qs = super()

class GreetingView(View):
	greeting = 'Good Day'
	template_name = 'courses/manage/course/list.html'
	
	def get(self, request):
		return HttpResponse(self.greeting)
